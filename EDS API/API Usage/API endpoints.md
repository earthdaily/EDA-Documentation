# STAC Endpoints

The base URL of the STAC catalog is https://api.eds.earthdaily.com/archive/v1/stac/v1 and below are various endpoints

* [Collections](#collections)
* [Collection](#collection) 
* [Items](#items)
* [Item](#item)
* [Queryables](#queryables)
* [Search](#search)
    * [Basic Search via GET Method]
    * [Basic Search via POST Method]
    * [Query Extension via POST Method]
    * [Fields Extension]
    * [Sortby Extension]
* [Queryables]
* [Downloading Assets]

## Collections 
Return list of all Collections
```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/collections
```
**Example** : [Command Line](Command%20Line.md#collections) | [Postman](Postman.md#collections) 

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
| CBERS-4 Mux L1C   | https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/cbers4-mux |

Example : [Command Line](Command%20Line.md#collection) | [Postman](Postman.md#collection) 


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
| CBERS-4 | https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/cbers4-mux/items |

The response also contains a link to the next set of items 

![NextItems](../../Images/STAC%20API/Postman%20Examples/LinksToNextItem.png)

Example : [Command Line](Command%20Line.md#items) | [Postman](Postman.md#items) 


## Item 
Returns a single Item for a given Collection and Item ID
```
GET https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/<COLLECTION_ID>/items/<ITEM_ID>
```
Example : [Command Line](Command%20Line.md#item) | [Postman](Postman.md#item) 

## Queryables 
Returns the queryable names for the STAC API Item Search using Query Extension
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

Example : [Command Line](Command%20Line.md#queryables) | [Postman](Postman.md#queryables) 


## Search  





