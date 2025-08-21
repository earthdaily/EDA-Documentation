---
layout: default
title: Python Samples
grand_parent: API
parent: API endpoints
nav_order: 3
---

## Python

For Python environments, we recommend using the **[EarthDaily Python Client](https://pypi.org/project/earthdaily/)** which provides a unified interface for interacting with the EarthDaily platform.

### Installation

```bash
# Basic installation
pip install earthdaily

# Recommended installation with platform features
pip install earthdaily[platform]

# Full installation with all features
pip install earthdaily[platform,legacy]
```
### Environment Setup

Create a `.env` file in your project root:

```bash
# .env
EDS_CLIENT_ID=your_client_id
EDS_SECRET=your_client_secret
EDS_AUTH_URL=https://your-auth-url.com/oauth/token
EDS_API_URL=https://api.earthdaily.com
```

### Getting Started with EarthDaily Client

```python
from dotenv import load_dotenv
from earthdaily import EDSClient, EDSConfig

# Load environment variables from .env file
load_dotenv()

# Initialize client with configuration from environment variables
config = EDSConfig()
client = EDSClient(config)

# Alternative: Direct configuration without .env file
config = EDSConfig(
    client_id="your_client_id",
    client_secret="your_client_secret", 
    token_url="https://your-auth-url.com/oauth/token",
    api_url="https://api.earthdaily.com"
)
client = EDSClient(config)
```



### Get Collections

```python
# Get all collections using the platform client
collections = client.platform.pystac_client.get_collections()
for collection in collections:
    print(f"Collection: {collection.id} - {collection.description}")
```

### Get a Specific Collection 

```python
# Get specific collection
collection = client.platform.pystac_client.get_collection("sentinel-2-l2a")
print(f"Collection: {collection.id} - {collection.description}")
```

### Search 

Search for items using the modern client interface:

```python
# Search using the platform client
search_results = client.platform.pystac_client.search(
    collections=["sentinel-2-l2a", "sentinel-2-l1c"],
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
    max_items=100
)

# Process search results
items = list(search_results.items())
for index, item in enumerate(items):
    print(f"Item {index}: ID={item.id}, Cloud Cover={item.properties.get('eo:cloud_cover')}")
```

### Specific Item

```python
# Search for specific items by ID
search_results = client.platform.pystac_client.search(
    collections=["sentinel-2-l2a"],
    ids=["S2B_35XMG_20230615_1_L2A", "S2B_39XVJ_20230615_0_L2A", "S2B_27LZJ_20230615_0_L2A"]
)

items = list(search_results.items())
for index, item in enumerate(items):
    print(f"Specific item {index}: ID={item.id}")
```

### Downloading Assets

The EarthDaily client provides seamless asset downloading with automatic handling of proxy URLs and presigned URLs:

#### Using the EarthDaily Client (Recommended)

```python
# Search for items with assets to download
search_results = client.platform.pystac_client.search(
    collections=["edc-preview"],
    datetime="2022-01-01T00:00:00Z/2023-01-01T00:00:00Z",
    max_items=5
)

items = list(search_results.items())

# Download assets using the client (automatically handles proxy/presigned URLs)
for item in items:
    print(f"Downloading assets for item: {item.id}")
    
    # Download specific assets
    downloads = client.platform.stac_item.download_assets(
        item=item,
        asset_keys=["image_file_R"],  # Specify which assets to download
        output_dir="./downloads",
        max_workers=3  # Parallel downloads
    )
    
    # Print download results
    for asset_key, download_path in downloads.items():
        print(f"Downloaded {asset_key} to: {download_path}")
```

#### Advanced Download Options

```python
# Download all assets from an item
downloads = client.platform.stac_item.download_assets(
    item=item,
    # asset_keys=None,  # Download all assets when not specified
    output_dir="./all_assets",
    max_workers=5,
    overwrite=True  # Overwrite existing files
)

# Download with custom naming
downloads = client.platform.stac_item.download_assets(
    item=item,
    asset_keys=["image_file_R", "image_file_G", "image_file_B", "image_file_NIR"],
    output_dir="./rgb_nir", 
    filename_template="{item_id}_{asset_key}.tif"  # Custom naming pattern
)
```
### Cloud Masks

```python
# Query sentinel-2-l2a for ag cloud masks using the client
search_results = client.platform.pystac_client.search(
    collections=["sentinel-2-l2a"],
    datetime="2022-07-01T00:00:00.000000Z/2022-08-01T00:00:00.000000Z",
    query={
        "eda:ag_cloud_mask_available": {
            "eq": True
        }
    },
    max_items=50
)

items = list(search_results.items())

print(f" Found {len(items)} items with agriculture cloud masks available")

```