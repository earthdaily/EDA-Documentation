---
layout: minimal
title: Commandline Samples
parent: API endpoints
nav_order: 1
---

## Command Line examples
The sections below include examples using [curl](https://curl.se/) commands. If a GUI is preferred, these commands can be [imported](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-with-curl-commands) into [Postman](https://www.postman.com/).

## Collections 
Return list of all Collections 

```
curl --location https://api.earthdaily.com/platform/v1/stac/collections --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'
```

## Collection

Return specific Collection 

Example curl request using access token generated in section above:

```

curl --location https://api.earthdaily.com/platform/v1/stac/collections/sentinel-2-l1c --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'

```

## Items 
Return paged Items ordered by datetime descending (It doesn’t support search parameters, so often /stac/v1/search is preferred instead)

```

curl --location https://api.earthdaily.com/platform/v1/stac/collections/sentinel-2-l1c/items --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'

```


## Item 
Returns a single Item for a given Collection and Item ID

```
curl --location https://api.earthdaily.com/platform/v1/stac/collections/sentinel-2-l1c/items/S2B_MSIL1C_20240422T190009_N0510_R027_T08JNQ_20240422T221641 --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'
```

## Queryables 
Returns the queryable names for the STAC API Item Search using Query Extension
Below are the two ways to query the “queryable items“ for a given collection

```
curl --location https://api.earthdaily.com/platform/v1/stac/collections/landsat-c2l1/queryables --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'
```

## Search  

Implements STAC basic Item search functionality  + extensions 

```
curl --location 'https://api.earthdaily.com/platform/v1/stac/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <ACCESS_TOKEN HERE>' \
--data '{
    "datetime": "2023-01-01T18:50:42.000000Z/2023-02-01T18:50:42.000000Z",
    "collections": ["sentinel-2-l1c","sentinel-2-l2a"],
    "intersects": {
        "coordinates": [
          [
            [
              -2.226934111129964,
              53.375337378064074
            ],
            [
              -2.226934111129964,
              50.0397331432938
            ],
            [
              3.334960050757161,
              50.0397331432938
            ],
            [
              3.334960050757161,
              53.375337378064074
            ],
            [
              -2.226934111129964,
              53.375337378064074
            ]
          ]
        ],
        "type": "Polygon"
      }
}'
```
### **[Query Extension](https://github.com/stac-api-extensions/query) via POST Method**

>EarthPlatform STAC API supports the [Query Extension](https://github.com/stac-api-extensions/query). It currently does not support the Filter Extension.

Advanced searching can be performed using a `query` object. This allows searching over supported properties on STAC items using various operators.

```
curl --location 'https://api.earthdaily.com/platform/v1/stac/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJraWQiOiJwdWlZR3BtalVETHFvdGVLR1wvbDM4SkJzMlVrdWVUb2VPS21EN1B4d1o0OD0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0dmowNHBwMnM0OWdsaGlnNnAxZ2VkZDNmbSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYWNjb3VudElkOnVzZXJJZFwvTTliTVlLYmlXRk4yZldBWnBlenhzdDozYTI1MmIzYjI2ZWQ0Y2FmYTI5ODA5ZWM3ZWExYzU2OCIsImF1dGhfdGltZSI6MTcxOTI1MTg5OCwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfeGN3T3dseWlmIiwiZXhwIjoxNzE5MjU1NDk4LCJpYXQiOjE3MTkyNTE4OTgsInZlcnNpb24iOjIsImp0aSI6IjhkY2Y1NmY5LWU2Y2ItNDVmYS1hODY5LTMzZmY2OThlY2ExYiIsImNsaWVudF9pZCI6IjR2ajA0cHAyczQ5Z2xoaWc2cDFnZWRkM2ZtIn0.E41hOMFyESoS393u4GRCvySP6-aDvbyeBp6kdSPZ7tFQrxqthiByXy6NBN8plLmEFO1vqQHpu5gA6Gy3L0v7_ACZXa74LJk5MvbtTCmoMh9QlFrCkaTpjGmpzEIjDwn_KRumrhf5d_omE6GpeE6vrz4I9-jQ0_P9LO3IQH3CcVX61oRvd44MT-1jxgu4bM3mEinjGOMYfszOgaj4O5PZ1kwund-05yfAiUnM81D5tCRiPSXbiOMMhSy2g-E-75t6AXZhLJg_EmWtERZ2Kf3UT5YU5-MI34-yx2RkqgDYlhanbyUy-W2K0OLILJucKX-I5cpTzt24WCOnUc0aFS2r6w' \
--data '{
    "limit": 20,
    "collections": [
        "landsat-c2l2-sr"
    ],
    "query": {
        "view:sun_elevation": {
            "gt": 40,
            "lt": 60
        },
        "eo:cloud_cover": {
            "lt": 10
        }
    }
}'
```

### [Fields Extension](https://github.com/stac-api-extensions/fields)
The Fields Extension allows you to specify which fields are returned from the API, reducing data transfer size. 

```
curl --location 'https://api.earthdaily.com/platform/v1/stac/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <ACCESS_TOKEN HERE>' \
--data '{
    "fields": {
      "include": ["id", "properties.datetime", "assets.aot"]
    }
}'
```

Exclude 

```
curl --location 'https://api.earthdaily.com/platform/v1/stac/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <ACCESS_TOKEN HERE>' \
--data '{
    "fields": {
      "exclude": ["links", "geometry"]
    }
}'
```

### [Sortby Extension](https://github.com/stac-api-extensions/sort)
By default, Items are returned by `datetime` descending. Then by `id` ascending.

Sorting by property `eo:cloud_cover` is also supported on the `/search` endpoint:

```
curl --location 'https://api.earthdaily.com/platform/v1/stac/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <ACCESS_TOKEN HERE>' \
--data '{
    "sortby": [
        {
            "field": "properties.eo:cloud_cover",
            "direction": "asc"
        }
    ]
}'
```

## Downloading Assets

```
curl --location 'https://api.earthdaily.com/platform/v1/stac/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <ACCESS_TOKEN HERE>' \
--header 'X-Signed-Asset-Urls: true' \
--data '{
    "limit": 20,
    "collections": [
        "sentinel-2-l2a-cog-ag-cloud-mask"
    ]
}'

```

Example response
```
"assets": {
    "agriculture-cloud-mask": {
        "href": "s3://earthdaily-eds-edc-skyfox-generic/_PUBLIC/sentinel-2-l2a-cog-ag-cloud-mask/2017/09/09/S2A_MSIL2A_20170909T174911_N0001_R141_T13TFG_20200331T022338.SAFE_AG_CLOUD_MASK_20230412004218/S2A_MSIL2A_20170909T174911_N0001_R141_T13TFG_20200331T022338.SAFE_AG_CLOUD_MASK_20230412004218.tif",
        "alternate": {
            "download": {
                "href": "https://earthdaily-eds-edc-skyfox-generic.s3.amazonaws.com/_PUBLIC/sentinel-2-l2a-cog-ag-cloud-mask/2017/09/09/S2A_MSIL2A_20170909T174911_N0001_R141_T13TFG_20200331T022338.SAFE_AG_CLOUD_MASK_20230412004218/S2A_MSIL2A_20170909T174911_N0001_R141_T13TFG_20200331T022338.SAFE_AG_CLOUD_MASK_20230412004218.tif?AWSAccessKeyId=.....&Signature=.......&x-amz-security-........&Expires=1694739928"
            }
        }
        ....
    }
}
```

## Cloud Masks

```
curl --location 'https://api.earthdaily.com/platform/v1/stac/search' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <ACCESS_TOKEN HERE>' \
--data '{
    "collections": ["sentinel-2-l2a"],
    "query": {
            "eda:ag_cloud_mask_available": {
                "eq": true
            }
      }
}'
```