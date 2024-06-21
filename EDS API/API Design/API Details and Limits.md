# Performant Query Best Practices

## Specify collections
Limit the query to only the collections you need. The STAC API uses a database architecture partitioned by collection_id. The more collections that are specified in the query, the more database tables will have to be scanned.

In cases where you are querying multiple collections and paging through thousands of results, the database is often having to discard matches to fit in the paging limit.  It can often be more performant to run concurrent queries with individual collections.

## Datetime Range
The narrower the datetime range specified in your query, the fewer the number of results will need to be scanned. This is especially true for the following collections, which are sub-partitioned by year at the database level.

* auxiliary-atmosphere
* cbers4-mux
* ecmwf-mars
* ecmwf-open-data
* goes
* himawari-l1b
* himawari-l2-cloud
* landsat-c2l1
* landsat-c2l2-sr
* landsat-c2l2-st
* landsat-l2-cog-ag-cloud-mask
* modis-43a4-061
* modis-aqua-calibrated-radiance
* modis-calibrated-radiance
* modis-mod04-l2-061
* modis-mod07-l2-061
* modis-mod35-l2-061
* modis-myd35-l2-061
* msg-seviri
* msg-seviri-cloud-mask
* sentinel-1-grd
* sentinel-1-rtc
* sentinel-2-l1c
* sentinel-2-l1c-ml-cloud-mask
* sentinel-2-l2a
* sentinel-2-l2a-cog-ag-cloud-mask
* sentinel-2-l2a-cog-ag-cloud-mask-geosys-private
* venus-l2a

## Use fields extension
Using the fields extension to only get the fields you need can result in dramatic reductions in database network traffic, and network traffic between you and the API.

## Only request Signed URLs when needed
Signing asset URLs has a performance impact. For collections with high numbers of assets, this additional latency can be multiple seconds

## ID Batching 
When trying to get multiple items by id, you can likely get better performance by batching requests with multiple values in ids 

Similarly, when searching for values by properties values. The in_ query support can be used.   

