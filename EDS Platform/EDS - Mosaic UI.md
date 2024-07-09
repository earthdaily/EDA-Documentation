# Table of Contents
* [Introduction]
* [Mosaic Preview Order]
* [Mosaic Full resolution Order]

## Introduction
[**EarthMosaics**](https://earthplatform.eds.earthdaily.com/ecommerce) delivers cloud-free, temporally coherent mosaics with ​the highest possible geolocation, radiometric ​quality, enabling users to examine true signals, minimize false positives in change detection, and easily contextualize with other geospatial datasets. From analysing a regional forest to monitoring a mining site, predicting water reservoir levels to measuring melting permafrost, EarthMosaics (now in beta) offers application-specific and customized insights fulfilling unique needs of each use case.

Analysis Ready Mosaics are complex, costly to produce, and designed to feed directly into ML applications​.

[EarthMosaics](https://earthplatform.eds.earthdaily.com/ecommerce)  from EarthDaily Analytics provides you a way to explore and get a free preview and you can also place ordewrs for full resolution Mosaics. 

## Getting started with Mosaics / Mosaic Preview Order

Below is the landing page you see when you navigate to [EarthMosaics](https://earthplatform.eds.earthdaily.com/ecommerce)

![WelcomeMosaics](../Images/EarthMosaics%20UI/WelcometoMosaic.png)

When you are the first time user, you get the Welcome dialog with an option to GetStarted

Pressing the `GetStarted` will take you to a NewOrders page. Lets see what all options we have while placing the order as below

![MosaicsOrderSetup](../Images/EarthMosaics%20UI/MosaicOrderSetup.png)

| S. No     | Label     | Description       |
|-----------|-----------|-------------------|
| <span style="background-color:orange"> " 1 "  </span> | Area of Interest | You can start drawing a polygon for your mosaics order. The limit currently is < 100,000 km<sup>2</sup>   |
| <span style="background-color:orange"> " 2 "  </span> | GeoJSON | Instead of drawing a polygon, if you have an existing GeoJSON, you have an option to enter it here. The restriction of < 100,000 km<sup>2</sup> applies to this too |
| <span style="background-color:orange"> " 3 "  </span> | Time of Interest | Specify the time of interest for your Mosaics order |
| <span style="background-color:orange"> " 4 "  </span> | Settings | This one gives you multiple choices to place your order as per your needs|

<br></br>
The area of interest (AOI) defines the geographic extent used to build the mosaic. You can either draw the AOI on the map or provide the AOI's GeoJSON below. To draw, start by left-clicking on the map. After adjusting the extent of your AOI, complete the AOI by left-clicking. Once drawn, you can select your AOI to reshape its boundaries.
<br></br>

![AoI](../Images/EarthMosaics%20UI/AoI.png)
<br></br>

![GeoJSON](../Images/EarthMosaics%20UI/GeoJSON.png)
<br></br>

![ToI](../Images/EarthMosaics%20UI/ToI.png)


The settings define how your mosaic will be generated. 
* Resolution determines the quality of your mosaic: Preview is free, whereas Full is paid. You are advised to first create a Preview Resolution mosaic, with your desired settings, to preview your order. 
* Processing type determines the pixel selection process: 
    * Best Measurement uses pixel-by-pixel weighting 
    * Peak NDVI uses Normalized Vegetation Index (NDVI)
    * Peak Burn Severity uses Normalized Burn Ratio (NBR) and 
    * Percentile uses a common pixel approach. 
* Source specifies if your mosaic will be made using only Sentinel-2A or the combination of Sentinel-2A and Landsat-8/9.
<br></br>

![Settings](../Images/EarthMosaics%20UI/Settings.png)

Now, after you confirm all settings, submit the order
<br></br>

![Submit](../Images/EarthMosaics%20UI/Submit.png)

Once you submit your order, you will see that your order is in Processing state. There is a button on top right of the panel if you want to check out all of your Mosaic Orders
<br></br>

![Processing](../Images/EarthMosaics%20UI/Processing.png)

Mosaic "All Oders" page below
<br></br>
![AllOrders](../Images/EarthMosaics%20UI/All%20Orders.png)

The orderId you see in this page can be found as a LineItemId in your AccountInformation page under "MyOrders"

![MyOrders](../Images/EarthMosaics%20UI/MyOrders.png)





## Mosaic Full resolution Order