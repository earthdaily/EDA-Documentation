## Command Line examples
The sections below include examples using [curl](https://curl.se/) commands. If a GUI is preferred, these commands can be [imported](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-with-curl-commands) into [Postman](https://www.postman.com/).

## Collections 
Return list of all Collections 

```
curl --location https://api.eds.earthdaily.com/archive/v1/stac/v1/collections --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'
```


## Collection

Return specific Collection 

Example curl request using access token generated in section above:

```

curl --location https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/sentinel-2-l1c --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'

```

## Items 
Return paged Items ordered by datetime descending (It doesn’t support search parameters, so often /stac/v1/search is preferred instead)

```

curl --location https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/sentinel-2-l1c/items --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'

```


## Item 
Returns a single Item for a given Collection and Item ID

```
curl --location https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/sentinel-2-l1c/items/S2B_MSIL1C_20240422T190009_N0510_R027_T08JNQ_20240422T221641 --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'
```

## Queryables 
Returns the queryable names for the STAC API Item Search using Query Extension
Below are the two ways to query the “queryable items“ for a given collection

```
curl --location https://api.eds.earthdaily.com/archive/v1/stac/v1/collections/landsat-c2l1/queryables --header 'Authorization: Bearer <ACCESS_TOKEN HERE>'
```

## Search  
