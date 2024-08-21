---
layout: default
title: Python Samples
parent: API endpoints
nav_order: 3
---

## Python
For Python environments, we recommend using [PySTAC Client](https://pystac-client.readthedocs.io/en/stable/#). Complete examples of using PySTAC Client with EarthPlatform STAC API are included: 

[earthplatform_stac_api_example](./earthplatform_stac_api_examples.py)   

Below are the various sections of the script in reagrds to STAC endpoints

### Getting the authentication token for Pystac Client

```
# Generate auth token

def get_new_token():
    token_req_payload = {'grant_type': 'client_credentials'}
    token_response = requests.post(auth_token_url,
    data=token_req_payload, verify=False, allow_redirects=False,
    auth=(client_id, client_secret))
    token_response.raise_for_status()

    tokens = json.loads(token_response.text)
    return tokens['access_token']

token = get_new_token()

# Configure pystac client

client = Client.open(api_url, headers={
    "Authorization": f"Bearer {token}"
})
```

### Get collections

```
for collection in client.get_all_collections():
    print(collection)
```

### Get a specific collection 
```
collection = client.get_collection("sentinel-2-l2a")
print(collection)
```

### Search 

Search a collection with different filter criteria, setting query with field conditions and sorting
```
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
).get_items()

for index, item in enumerate(items):
    print(f"{index}, {item}")
```

### Specific Item

```
items = client.search(
    collections=["sentinel-2-l2a"],
    ids=["S2B_35XMG_20230615_1_L2A", "S2B_39XVJ_20230615_0_L2A", "S2B_27LZJ_20230615_0_L2A"]
).get_items()

for index, item in enumerate(items):
    print(f"{index}, {item}")
```

### Cloud Masks

```
# Query sentinel-2-l2a for ag cloud masks

items = client.search(
    collections=["sentinel-2-l2a"],
    query={
        "eda:ag_cloud_mask_available": {
            "eq": True
        }
    },
    max_items=50
).get_items()

for index, item in enumerate(items):
    print(item)
    cloud_mask_item = client.get_collection(item.properties["eda:ag_cloud_mask_collection_id"]
                                            ).get_item(item.properties["eda:ag_cloud_mask_item_id"])

    print(cloud_mask_item)

```