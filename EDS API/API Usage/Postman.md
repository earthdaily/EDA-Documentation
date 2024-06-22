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


