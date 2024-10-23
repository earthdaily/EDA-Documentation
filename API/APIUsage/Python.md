---
layout: default
title: Python Samples
grand_parent: API
parent: API endpoints
nav_order: 3
---

## Python
For Python environments, we recommend using [PySTAC Client](https://pystac-client.readthedocs.io/en/stable/#). Complete examples of using PySTAC Client with EarthPlatform STAC API are included: 

[earthplatform_stac_api_example](https://github.com/earthdaily/EDA-Documentation/tree/gh-pages/API/APIUsage/earthplatform_stac_api_examples.py)   

Below are the various sections of the script in reagrds to STAC endpoints

### Getting the authentication token for Pystac Client

```python
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_TOKEN_URL = os.getenv("ACCESS_TOKEN_URL")
API_URL = os.getenv("EDS_API_URL")

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
        print(f"Failed to obtain token: {e}")

token = get_new_token(session)

catalog = Client.open(API_URL, headers={"Authorization": f"bearer {token}"})
```

### Get collections

```python
for collection in client.get_all_collections():
    print(collection)
```

### Get a specific collection 
```python
collection = client.get_collection("sentinel-2-l2a")
print(collection)
```

### Search 

Search a collection with different filter criteria, setting query with field conditions and sorting
```python
items = client.search(
    collections=["sentinel-2-l2a", "sentinel-l1c"],
    datetime="2022-07-01T00:00:00.000000Z/2023-08-01T00:00:00.000000Z",
    intersects={
        "coordinates": [
            [
                [
                    -124.18953337119558,
                    49.734095507050256
                ],
                [
                    -124.18953337119558,
                    48.73413273779468
                ],
                [
                    -121.93408220580699,
                    48.73413273779468
                ],
                [
                    -121.93408220580699,
                    49.734095507050256
                ],
                [
                    -124.18953337119558,
                    49.734095507050256
                ]
            ]
        ],
        "type": "Polygon"
    },
    # Cloud cover less than 10%
    query={
        "eo:cloud_cover": {
            "lt": 10
        }
    },
    sortby=[
        {
            "field": "properties.eo:cloud_cover",
            "direction": "asc"
        }
    ],
    limit=50,  # This is the number of items to be returned per page
    max_items=100,  # This is number of items to page over
).items()

for index, item in enumerate(items):
    print(f"{index}, {item}")
```

### Specific Item

```python
items = client.search(
    collections=["sentinel-2-l2a"],
    ids=["S2B_35XMG_20230615_1_L2A", "S2B_39XVJ_20230615_0_L2A", "S2B_27LZJ_20230615_0_L2A"]
).items()

for index, item in enumerate(items):
    print(f"{index}, {item}")
```

### Cloud Masks

```python
# Query sentinel-2-l2a for ag cloud masks

items = client.search(
    collections=["sentinel-2-l2a"],
    query={
        "eda:ag_cloud_mask_available": {
            "eq": True
        }
    },
    max_items=50
).items()

for index, item in enumerate(items):
    print(item)
    cloud_mask_item = client.get_collection(item.properties["eda:ag_cloud_mask_collection_id"]
                                            ).get_item(item.properties["eda:ag_cloud_mask_item_id"])

    print(cloud_mask_item)

```