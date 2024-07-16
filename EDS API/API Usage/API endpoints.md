# STAC Endpoints

The base URL of the STAC catalog is https://api.eds.earthdaily.com/archive/v1/stac/v1 and below are various endpoints

* [Collections](#collections)
* [Collection](#collection) 
* [Items](#items)
* [Item](#item)
* [Queryables](#queryables)
* [Search](#search)
    * [Basic Search via GET Method](#basic-search-via-get-method)
    * [Basic Search via POST Method](#basic-search-via-post-method)
    * [Query Extension via POST Method](#query-extension-via-post-method)
    * [Fields Extension](#fields-extension)
    * [Sortby Extension](#sortby-extension)
* [Downloading Assets](#downloading-assets)
* [Cloud Mask Query](#cloud-mask-query)

## Collections 
Return list of all Collections
```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/collections
```
**Example** : [Command Line](Command%20Line.md#collections) | [Postman](Postman.md#collections) | | [Python](./Python.md#get-collections)

## Collection 
Return specific Collection

```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/<COLLECTION_ID>
```

This end point takes the collection id as parameter. Below are some examples

| Collection | URL |
|------------------------------|--------------------------------------------------------------------|
| Sentinel-2 L1C | https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/sentinel-2-l1c |
| Landsat Collection 2 L1 | https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/landsat-c2l1 |

Example : [Command Line](Command%20Line.md#collection) | [Postman](Postman.md#collection) | [Python](./Python.md#get-a-specific-collection)


## Items 
Return paged Items ordered by datetime descending (It doesn’t support search parameters, so often /stac/v1/search is preferred instead)
```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/<COLLECTION_ID>/items
```

This end point takes the collection id as parameter. Below are some examples

|  Collection |  URL | 
|----------------------|-------------------|
| Sentinel-2 | https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/sentinel-2-l1c/items |
| Landsat Collection 2 L1 | https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/landsat-c2l1/items |

The response also contains a link to the next set of items 

![NextItems](../../Images/STAC%20API/Postman%20Examples/LinksToNextItem.png)

Example : [Command Line](Command%20Line.md#items) | [Postman](Postman.md#items) 


## Item 
Returns a single Item for a given Collection and Item ID
```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/<COLLECTION_ID>/items/<ITEM_ID>
```
Example : [Command Line](Command%20Line.md#item) | [Postman](Postman.md#item) | [Python](./Python.md#specific-item)

## Queryables 
Returns the queryable names for the STAC API Item Search using Query Extension. which allows you to discover which properties are queryable for all collections, a specific collection, or an intersection of collections.

Below are the two ways to query the “queryable items“ for a given collection

```

GET https://api.eds.earthdaily.com/archive/v1/stac/v1/queryables?collections=<COLLECTION_ID>
```
or
```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/{collection_id}/queryables
```

Parameters:
collectionId Matches against Item collectionId values 

The queryables endpoint  includes the datatype that must be used.

The queryables endpoint currently doesn’t provide information on supported operations for a given property/datatype. Supplying an unsupported field-value-operation combination will result in an error 400 (Bad Request) being returned. Example: a `contains` operation is not supported on a `string` queryable.

* Get queryable properties that apply to all collections: 
`https://api.eds.earthdaily.com/archive/v1/stac/v1/queryables`  

* Get queryable fields that apply to collection sentinel-2-l2a:
`https://api.eds.earthdaily.com/archive/v1/stac/v1/queryables?collections=sentinel-2-l2a`  

* Get queryable fields that apply to both collections sentinel-2-l1c and sentinel-2-l2a:
`https://api.eds.earthdaily.com/archive/v1/stac/v1/queryables?collections=sentinel-2-l1c,sentinel-2-l2a`

</br>
Example : [Command Line](Command%20Line.md#queryables) | [Postman](Postman.md#queryables) 


## Search  

Implements STAC basic Item search functionality  + extensions 

> !  For performance, it is highly recommended that your search requests is constrained by a collections parameter. This may be enforced in future.

**Parameters:**

* collections Matches against Item collection values (treated as OR causes)
* ids Matches against Item id values (treated as OR causes)
* datetime All dates must be in RFC 3339 format
    * Can be exact date match datetime=2023-05-14T18:50:42.000000Z 
    * Can be from-to datetime=2023-01-01T18:50:42.000000Z/2023-02-01T18:50:42.000000Z 
    * Can be from datetime=2023-01-01T18:50:42.000000Z..
    * Can be to datetime=..2023-01-01T18:50:42.000000Z
* bbox Matches against intersecting Item bbox values
* intersects (GeoJSON) Matches against intersecting Item geometry values (supported on POST method only)
* limit number of records to be returned

### **Basic Search via GET Method**

Shows use of datetime, collections and bbox

```
https://api.eds.earthdaily.com/archive/v1/stac/v1/search?datetime=2023-01-01T18:50:42.000000Z/2023-02-01T18:50:42.000000Z&bbox=-1.757813,51.971346,-0.065918,52.589701&collections=sentinel-2-l1c,sentinel-2-l2a
```
### **Basic Search via POST Method**

Shows use of datetime, collections and intersects

Example : [Command Line](Command%20Line.md#search) | [Postman](Postman.md#search) | [Python](./Python.md#search)


### **[Query Extension](https://github.com/stac-api-extensions/query) via POST Method**

>EarthPlatform STAC API supports the [Query Extension](https://github.com/stac-api-extensions/query). It currently does not support the Filter Extension.

Advanced searching can be performed using a `query` object. This allows searching over supported properties on STAC items using various operators.

When searching across 1 or more Collections, and a field is specified which is not supported, no items will be returned for that Collection. 

To discover which fields are queryable on each Collection, see Queryables.  

Query Extension syntax:

```
{
    ... 
    "query": {
        "<QUERYABLE_PROPERTY_1>": {
            "OPERATOR_1": "VALUE",
            "OPERATOR_2": "VALUE"
        },
        "<QUERYABLE_PROPERTY_2>": {
            "OPERATOR": "VALUE"
        }
    }
}
```
\
Query Extension example: 

```
{
    "query": {
        "view:sun_elevation": {
            "gt": 40,
            "lt": 60
        },
        "eo:cloud_cover": {
            "lt": 10
        }
    }
}
```
Each property and each operation is treated as an `AND` cause

So the above would result in a query of `view:sun_elevation > 40 AND view:sun_elevation < 60 AND eo:cloud_cover < 10`

Example : [Command Line](Command%20Line.md#query-extension-via-post-method) | [Postman](Postman.md#query-extension-via-post-method) | | [Python](./Python.md#search)


????? **Supported Operators** do we need the table?

### [Fields Extension](https://github.com/stac-api-extensions/fields)
The Fields Extension allows you to specify which fields are returned from the API, reducing data transfer size. 

>Use of Fields Extension allows returning items in a potentially non-STAC compliant format. This can cause exceptions in PySTAC Client.

Example - only return `id`, `properties.datetime` and `assets.aot`

```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/search?fields=id,properties.datetime,assets.aot
```
POST example

Example - exclude `links` and `geometry`

```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/search?fields=-links,-geometry
```
POST example

Example : [Command Line](Command%20Line.md#fields-extension) | [Postman](Postman.md#fields-extension) | [Python](./Python.md#search)

### [Sortby Extension](https://github.com/stac-api-extensions/sort)
By default, Items are returned by `datetime` descending. Then by `id` ascending.

Sorting by property `eo:cloud_cover` is also supported on the `/search` endpoint:

GET examples:

Sortby `eo:cloud_cover` ascending:

GET https://api.eds.earthdaily.com/stac/v1/search?sortby=eo:cloud_cover

Sortby `eo:cloud_cover` descending:
GET https://api.eds.earthdaily.com/stac/v1/search?sortby=-eo:cloud_cover

> When sorting by `eo:cloud_cover`, only items with non-null `eo:cloud_cover` property values will be returned.

Example : [Command Line](Command%20Line.md#sortby-extension) | [Postman](Postman.md#sortby-extension) | [Python](./Python.md#search)

## Downloading Assets
The STAC `assets` property will contain `href`s to files on various hosts, depending on the original data provider. S3 hosted assets will have `s3://` protocol `href`s *

*we are currently in the process of migrating to this consistent main `href` format. At the moment a combination of `https://` and `s3://` are returned.

An S3 `https://` version of the URL be be available as an [alternate asset](https://github.com/stac-extensions/alternate-assets) . With a key of `download_url`

For private and requester pays S3 assets, and Azure Blob assets, we offer presigned URLs.

> Presigned URLs are returned by default on the `/items/{item_id}` endpoint but are not returned by default on the `/search` and `/items` endpoints as there is a performance latency and response size cost.

>Use a `X-Signed-Asset-Urls` boolean header to override default behaviour. Be aware a high `limit` parameter on the search endpoint combined with a high asset count collection can result in high response latency.

Presigned URLs are available for EDA buckets for all customer accounts. Presigned URLs for 3rd party buckets (example `s3://sentinel-s2-l1c`) are available depending on your account setup. Please note that these presigned URLs are valid for 12 hours after which they expire.

Example : [Command Line](Command%20Line.md#downloading-assets) | [Postman](Postman.md#downloading-assets) 
 

 ## Cloud Mask Query

 You can use the post Query method above to  get the earthdaily cloud masks as well.
 
Example : [Command Line](Command%20Line.md#cloud-masks) | [Postman](Postman.md#cloudmasks) | [Python](./Python.md#cloud-masks)
