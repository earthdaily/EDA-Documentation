import logging
import os

import requests
from pystac_client import Client

# Logger configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Loading secrets from environment variables
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_TOKEN_URL = os.getenv("ACCESS_TOKEN_URL")
API_URL = "https://api.earthdaily.com/platform/v1/stac"

# Setup requests session
session = requests.Session()
session.auth = (CLIENT_ID, CLIENT_SECRET)


def get_new_token(session):
    """Obtain a new authentication token using client credentials."""
    token_req_payload = {"grant_type": "client_credentials"}
    try:
        token_response = session.post(AUTH_TOKEN_URL, data=token_req_payload)
        token_response.raise_for_status()
        tokens = token_response.json()
        return tokens["access_token"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to obtain token: {e}")
        exit(1)


def initialize_stac_client(api_url, token):
    """Initialize and return a configured PySTAC client."""
    return Client.open(api_url, headers={"Authorization": f"Bearer {token}"})


def main():
    token = get_new_token(session)
    client = initialize_stac_client(API_URL, token)

    try:
        # Get all collections
        for collection in client.get_all_collections():
            logger.info(collection)

        # Get specific collection
        collection = client.get_collection("sentinel-2-l2a")
        logger.info(collection)

        # Perform a search
        items = client.search(
            collections=["sentinel-2-l2a", "sentinel-1c"],
            datetime="2022-07-01T00:00:00.000000Z/2023-08-01T00:00:00.000000Z",
            intersects={
                "coordinates": [
                    [
                        [-124.18953337119558, 49.734095507050256],
                        [-124.18953337119558, 48.73413273779468],
                        [-121.93408220580699, 48.73413273779468],
                        [-121.93408220580699, 49.734095507050256],
                        [-124.18953337119558, 49.734095507050256],
                    ]
                ],
                "type": "Polygon",
            },
            query={"eo:cloud_cover": {"lt": 10}},
            sortby=[{"field": "properties.eo:cloud_cover", "direction": "asc"}],
            limit=50,
            max_items=100,
        ).get_items()

        for index, item in enumerate(items):
            logger.info(f"{index}, {item}")

        # Query for specific items
        items = client.search(
            collections=["sentinel-2-l2a"],
            ids=[
                "S2B_35XMG_20230615_1_L2A",
                "S2B_39XVJ_20230615_0_L2A",
                "S2B_27LZJ_20230615_0_L2A",
            ],
        ).get_items()

        for index, item in enumerate(items):
            logger.info(f"{index}, {item}")

        # Query for cloud masks
        items = client.search(
            collections=["sentinel-2-l2a"],
            query={"eda:ag_cloud_mask_available": {"eq": True}},
            max_items=50,
        ).get_items()

        for index, item in enumerate(items):
            logger.info(item)
            cloud_mask_item = client.get_collection(
                item.properties["eda:ag_cloud_mask_collection_id"]
            ).get_item(item.properties["eda:ag_cloud_mask_item_id"])

            logger.info(cloud_mask_item)

    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
