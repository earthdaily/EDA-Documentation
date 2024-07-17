---
layout: minimal
title: Postman Samples
parent: API endpoints
nav_order: 2
---

## Postman Examples
Before you try out the various endpoints, you need to set up the authentication for the Postman. [Authentication Page](../../Getting%20Started/API%20Authentication.md#postman) describes how it is done.

## Collections 
Return list of all Collections 

![Collections](../../Images/STAC%20API/Postman%20Examples/Collections.png)

## Collection

Return specific Collection 

![Collections](../../Images/STAC%20API/Postman%20Examples/Collection.png)


## Items 
Return paged Items ordered by datetime descending (It doesn’t support search parameters, so often /stac/v1/search is preferred instead)

![Collections](../../Images/STAC%20API/Postman%20Examples/Items.png)


## Item 
Returns a single Item for a given Collection and Item ID

![Collections](../../Images/STAC%20API/Postman%20Examples/ItemId%20.png)


## Queryables 
Returns the queryable names for the STAC API Item Search using Query Extension
Below are the two ways to query the “queryable items“ for a given collection

![Collections](../../Images/STAC%20API/Postman%20Examples/Queryables.png)


## Search  

Implements STAC basic Item search functionality  + extensions 

Ensure the **content-type** header is **application/json**

![Collections](../../Images/STAC%20API/Postman%20Examples/Post%20Search%20With%20Data.png)

### **[Query Extension](https://github.com/stac-api-extensions/query) via POST Method**

>EarthPlatform STAC API supports the [Query Extension](https://github.com/stac-api-extensions/query). It currently does not support the Filter Extension.

Advanced searching can be performed using a `query` object. This allows searching over supported properties on STAC items using various operators.

![Collections](../../Images/STAC%20API/Postman%20Examples/Query%20Extension.png)


### [Fields Extension](https://github.com/stac-api-extensions/fields)
The Fields Extension allows you to specify which fields are returned from the API, reducing data transfer size. 

![Collections](../../Images/STAC%20API/Postman%20Examples/Field%20Extension%20ID.png)

Exclude 

![Collections](../../Images/STAC%20API/Postman%20Examples/Field%20Extension%20Exclude.png)


### [Sortby Extension](https://github.com/stac-api-extensions/sort)
By default, Items are returned by `datetime` descending. Then by `id` ascending.

Sorting by property `eo:cloud_cover` is also supported on the `/search` endpoint:

| asc|asc|
|----|---|
| ![Collections](../../Images/STAC%20API/Postman%20Examples/Sort%20Asc%20.png) | ![Collections](../../Images/STAC%20API/Postman%20Examples/Sort%20Desc.png) |


## Downloading Assets

![Collections](../../Images/STAC%20API/Postman%20Examples/Downloading%20assets.png)

## CloudMasks

![Collections](../../Images/STAC%20API/Postman%20Examples/CloudMask.png)

