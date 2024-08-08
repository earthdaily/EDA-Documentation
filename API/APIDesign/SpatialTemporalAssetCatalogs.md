---
layout: minimal
title: STAC Specification
parent: EDS API
nav_order: 1
has_children: true
---

# The STAC Specification

STAC is the most commonly used standard across various GeoSpatial platforms for exchange and search of GeoTemporal data. 
[SpatioTemporal Asset Catalogs](https://stacspec.org/en) 

>  At its core, the SpatioTemporal Asset Catalog (STAC) specification provides a common structure for describing and cataloging spatiotemporal assets. A spatiotemporal asset is any file that represents information about the earth captured in a certain space and time.

The [**STAC Specification**](https://stacspec.org/en/about/stac-spec/) consists of 4 semi-independent specifications. Each can be used alone, but they work best in concert with one another.

* [STAC Item](https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md) is the core atomic unit, representing a single spatiotemporal asset as a GeoJSON feature plus datetime and links.

* [STAC Catalog](https://github.com/radiantearth/stac-spec/blob/master/catalog-spec/catalog-spec.md) is a simple, flexible JSON file of links that provides a structure to organize and browse STAC Items. A series of best practices helps make recommendations for creating real world STAC Catalogs.

* [STAC Collection](https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md) is an extension of the STAC Catalog with additional information such as the extents, license, keywords, providers, etc that describe STAC Items that fall within the Collection.

* [STAC API](https://github.com/radiantearth/stac-api-spec) provides a RESTful endpoint that enables search of STAC Items, specified in OpenAPI, following OGC's WFS 3.

Earthdaily provide the STAC compliant API end points for integration with our EarthPipeline components. The information below will help in a better understanding of the STAC 

STAC Resources
* [Intro to STAC: an Overview of the Specification](https://stacspec.org/en/tutorials/intro-to-stac/)

* [SAT-API Browser](http://sat-api-browser.s3-website-us-east-1.amazonaws.com/)  

* [STAC API](https://api.stacspec.org/v1.0.0-rc.1/)

* [STAC Extensions](https://stac-extensions.github.io/)



Earthdaily has it's own EDA extension which is used for collections and items mainly

*  [EDA extension schema](../Extensions/EDA%20STAC%20extension%20schema.json)
*  [EDA extension details](../Extensions/EDASTACextension.md) 
*  [EDA Data Coverage extension schema](../Extensions/EDA%20Data%20Coverage%20STAC%20extension%20schema.json)
*  [EDA Data Coverage extension details](../Extensions/EDADataCoverageSTACextension.md)