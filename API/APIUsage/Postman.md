---
layout: minimal
title: Postman Samples
parent: API endpoints
nav_order: 2
---

## Postman Examples
Before you try out the various endpoints, you need to set up the authentication for the Postman. [Authentication Page](../../GettingStarted/APIAuthentication#postman) describes how it is done.

## Collections 
Return list of all Collections 

![Collections](../../Images/STACAPI/PostmanExamples/Collections.png)

## Collection

Return specific Collection 

![Collections](../../Images/STACAPI/PostmanExamples/Collection.png)


## Items 
Return paged Items ordered by datetime descending (It doesn’t support search parameters, so often /stac/v1/search is preferred instead)

![Collections](../../Images/STACAPI/PostmanExamples/Items.png)


## Item 
Returns a single Item for a given Collection and Item ID

![Collections](../../Images/STACAPI/PostmanExamples/ItemId.png)


## Queryables 
Returns the queryable names for the STAC API Item Search using Query Extension
Below are the two ways to query the “queryable items“ for a given collection

![Collections](../../Images/STACAPI/PostmanExamples/Queryables.png)


## Search  

Implements STAC basic Item search functionality  + extensions 

Ensure the **content-type** header is **application/json**

![Collections](../../Images/STACAPI/PostmanExamples/PostSearchWithData.png)

### **[Query Extension](https://github.com/stac-api-extensions/query) via POST Method**

>EarthPlatform STAC API supports the [Query Extension](https://github.com/stac-api-extensions/query). It currently does not support the Filter Extension.

Advanced searching can be performed using a `query` object. This allows searching over supported properties on STAC items using various operators.

![Collections](../../Images/STACAPI/PostmanExamples/QueryExtension.png)


### [Fields Extension](https://github.com/stac-api-extensions/fields)
The Fields Extension allows you to specify which fields are returned from the API, reducing data transfer size. 

![Collections](../../Images/STACAPI/PostmanExamples/FieldExtensionID.png)

Exclude 

![Collections](../../Images/STACAPI/PostmanExamples/FieldExtensionExclude.png)


### [Sortby Extension](https://github.com/stac-api-extensions/sort)
By default, Items are returned by `datetime` descending. Then by `id` ascending.

Sorting by property `eo:cloud_cover` is also supported on the `/search` endpoint:

| Asc|Desc|
|----|---|
| ![Collections](../../Images/STACAPI/PostmanExamples/SortAsc.png) | ![Collections](../../Images/STACAPI/PostmanExamples/SortDesc.png) |


## Downloading Assets

![Collections](../../Images/STACAPI/PostmanExamples/DownloadingAssets.png)

## CloudMasks

![Collections](../../Images/STACAPI/PostmanExamples/CloudMask.png)

