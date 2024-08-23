---
layout: default
title: Quick Start
grand_parent: EDS Documentation
parent: Getting Started
nav_order: 3
---
# Table of contents
* [EarthDaily Data](#earthdaily-data)
* [Authentication](#authentication)
* [API](#api)
* [Pystac](#pystac)
* [EarthDaily Python Client](#earthdaily-python-client)
    * [Other Examples](#other-examples)

## EarthDaily Data

EarthDaily data comprises of Open collections, EDA specific collections, Mosaics and Cloudmasks. There are different ways to access this data and they are outlined below. Please note that for all of the below options, you will need to have authentication details available. You can find the details about all the available [Collections](../Collections/AvailableCollections.md), [Mosaics](../Collections/EDAMosaics.md) and [CloudMasks](../Collections/EDACloudMasks.md).

1. API
2. PySTAC library
3. EarthDaily Python Client

## Authentication

There are different ways outlined below for accessing the EarthDaily data. . The required client_id, client_secret and access_token_url values can be found on [Account Management](https://console.earthdaily.com/account) page. These API credentials are specific to your user account on EarthPlatform and should be kept confidential.

![Client Credentials](../Images/STACAPI//AccountInformation.png)
For more see: [Authentication](../GettingStarted/APIAuthentication.md)

## API

Earthdaily provides STAC compliant restful APIs with various endpoints for you to access the data. You can also search the data with specific filters on fields and customize the output to include the data you are interested in. Find the detailed list of endpoints along with the examples. 

[API list](../API/APIUsage/Endpoints.md) gives you the detailed list of available endpoints

[Postman Examples](../API/APIUsage/Postman.md) are available to se the example query and the response using Postman

[Curl Examples](../API/APIUsage/CommandLine.md) are available in case you are interested to play around with our APIs using commandline 

## PySTAC

PySTAC is a library for working with [SpatioTemporal Asset Catalogs (STAC)](https://stacspec.org/en). Please find all the features and capabilities of [PySTAC](https://pystac.readthedocs.io/en/stable/) along with the details of all the set up required.

Here is a small snippet to give you an idea

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

# Get collections

for collection in client.get_all_collections():
    print(collection)
```

You can find the detailed examples using [Python script](../API/APIUsage/Python.md)

## EarthDaily Python Client

The fastest way to get up and running is to use EDA's [Python Client Repository](https://github.com/earthdaily/earthdaily-python-client). 

Build a new Conda Environment:
```
# Clone the repository and go inside
git clone git@github.com:earthdaily/earthdaily-python-client.git
cd earthdaily-python-client

# Create a virtual environment named earthdaily and install package dependencies
conda env create -n earthdaily -f requirements.yml
conda activate earthdaily

# Install package in editable mode
pip install -e .

copy-earthdaily-credentials-template --default

```


Test the Available Collections:
```
"""
from earthdaily.earthdatastore.cube_utils import asset_mapper
from rich.table import Table
from rich.console import Console

console = Console(force_interactive=True)

for collection, assets in asset_mapper._asset_mapper_config.items():
    table = Table(
        "asset",
        "EarthDaily Common band name",
        title=f"Earthdaily common names for {collection}",
    )
    for common_name, asset in assets[0].items():
        table.add_row(asset, common_name)
    console.print(table)
```

This will output a list of assets for all available collections to you in the platform.

![Python Example Band Names](../Images/STACAPI/pythonexamplebandnames.png)

## Other Examples


1. [Common Band Names](https://github.com/earthdaily/earthdaily-python-client/blob/main/examples/common_band_names.py)
2. [Compare Scale with Sentinel-2](https://github.com/earthdaily/earthdaily-python-client/blob/main/examples/compare_scale_s2.py)
3. [EarthDaily Simulated Datasets](https://github.com/earthdaily/earthdaily-python-client/blob/main/examples/earthdaily_simulated_dataset.py)
4. [Field Evolution](https://github.com/earthdaily/earthdaily-python-client/blob/main/examples/field_evolution.py)
5. [Create a Data Cube](https://github.com/earthdaily/earthdaily-python-client/blob/main/examples/first_steps_create_datacube.py)
6. [Create a Multisensor Cube](https://github.com/earthdaily/earthdaily-python-client/blob/main/examples/multisensors_cube.py)
7. [Stack Summary](https://github.com/earthdaily/earthdaily-python-client/blob/main/examples/summary_stack.py)

The fastest way to get up and running is to use EDA's [Python Client Repository](https://github.com/earthdaily/earthdaily-python-client). 
