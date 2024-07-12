# Table of Contents
* [Introduction](#introduction)
* [Getting started with Mosaics](#getting-started-with-mosaics)
* [Mosaic Preview Order](#mosaic-preview-order)
* [Mosaic Full resolution Order](#mosaic-full-resolution-order)
* [Managing Mosaics Order](#managing-mosaics-orders)

## Introduction
[**EarthMosaics**](https://earthplatform.eds.earthdaily.com/ecommerce) delivers cloud-free, temporally coherent mosaics with ​the highest possible geolocation, radiometric ​quality, enabling users to examine true signals, minimize false positives in change detection, and easily contextualize with other geospatial datasets. From analysing a regional forest to monitoring a mining site, predicting water reservoir levels to measuring melting permafrost, EarthMosaics (now in beta) offers application-specific and customized insights fulfilling unique needs of each use case.

Analysis Ready Mosaics are complex, costly to produce, and designed to feed directly into ML applications​.

[EarthMosaics](https://earthplatform.eds.earthdaily.com/ecommerce)  from EarthDaily Analytics provides you a way to explore and get a free preview and you can also place ordewrs for full resolution Mosaics. 

## Getting started with Mosaics

Below is the landing page you see when you navigate to [EarthMosaics](https://earthplatform.eds.earthdaily.com/ecommerce)

![WelcomeMosaics](../Images/EarthMosaics%20UI/WelcometoMosaic.png)

When you are the first time user, you get the Welcome dialog with an option to GetStarted

Pressing the `GetStarted` will take you to a NewOrders page. Lets see what all options we have while placing the order as below

![MosaicsOrderSetup](../Images/EarthMosaics%20UI/MosaicOrderSetup.png)

| S. No     | Label     | Description       |
|-----------|-----------|-------------------|
| ![](https://img.shields.io/static/v1?label=&message=1&color=orange)  | Area of Interest | You can start drawing a polygon for your mosaics order. The limit currently is < 100,000 km<sup>2</sup>   |
| <span style="background-color:orange"> " 2 "  </span> | GeoJSON | Instead of drawing a polygon, if you have an existing GeoJSON, you have an option to enter it here. The restriction of < 100,000 km<sup>2</sup> applies to this too |
| <span style="background-color:orange"> " 3 "  </span> | Time of Interest | Specify the time of interest for your Mosaics order |
| <span style="background-color:orange"> " 4 "  </span> | Settings | This one gives you multiple choices to place your order as per your needs|

<br></br>
The area of interest (AOI) defines the geographic extent used to build the mosaic. You can either draw the AOI on the map or provide the AOI's GeoJSON below. To draw, start by left-clicking on the map. After adjusting the extent of your AOI, complete the AOI by left-clicking. Once drawn, you can select your AOI to reshape its boundaries.
<br></br>

![AoI](../Images/EarthMosaics%20UI/AoI.png)
<br></br>

Once you draw a polygon, you will see the area calculator diaplays the total area selected by you. You will see three options appear 
| S. No     | Label     | Description       |
|-----------|-----------|-------------------|
| <span style="background-color:orange"> " 5 "   </span> | Fit Bounds | This option allows you to bring back the focus on the area drawn and fits it to the viewport    |
| <span style="background-color:orange"> " 6 "  </span> | GeoJSON | Instead of drawing a polygon, if you have an existing GeoJSON, you have an option to enter it here. The restriction of < 100,000 km<sup>2</sup> applies to this too |
| <span style="background-color:orange"> " 7 "  </span> | Delete | Delete the existing AoI |

<br></br>
![GeoJSON](../Images/EarthMosaics%20UI/GeoJSON.png)
<br></br>

![ToI](../Images/EarthMosaics%20UI/ToI.png)

## Mosaic Preview Order
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

## Mosaic Full resolution Order

Mosaics Full Resolution Order is very similar to the preview except that it has an additional step for payment.

As you will notice in the above images, the Preview order has mainly 2 steps
* Configuration
* Confirmation

Now, the Full Resolution Mosaic has an additional step 
* Quote

To place the Full resolution Mosaics order you will primarily use "Full" as your Resolution setting as shown below

![FullResOrder](../Images/EarthMosaics%20UI/FullResOrder.png)

Please confirm the order settings in order to checkout

![Checkout](../Images/EarthMosaics%20UI/Checkout.png)

The checkout screen below shows you the order price. If you are ready to pay, go ahead and chekout to get to the payment page below.

![Pay](../Images/EarthMosaics%20UI/Pay.png)

If you have any coupons to redeem, you can enter the coupon code in order to get the eligible discount. Once you are ok with total amount and have entered relevant payment details, please proceed to pay

## Managing Mosaics Orders

Once you have placed the Mosaic order (either Preview or Full), you will be redirected to your Dashboard where you can see all your orders.

![All Orders-Full](../Images/EarthMosaics%20UI/All%20Orders-Full.png)

Upon submission, you will see that your order is in Processing state. There is a button on top right of the panel if you want to View all of your Mosaic Orders


![AllOrders](../Images/EarthMosaics%20UI/All%20Orders.png)

The orderId you see in this page can be found as a LineItemId in your AccountInformation page under "MyOrders"

![MyOrders](../Images/EarthMosaics%20UI/MyOrders.png)

Once the order is processed successfully, you will see the state changed to "Processed" and some other options enabled for the order

![OrdersMgmt](../Images/EarthMosaics%20UI/OrdersMgmt.png)


| S.No        | Label     | Description       |
|--------------|-----------|-------------------|
| <span style="background-color:orange"> " 8 "  </span> | Copy | This option allows you to copy the order in case you want to use the same settings or have a minor modification to place another order     |
| <span style="background-color:orange"> " 9 "  </span> | Download | This is where you can download your product - preview or full |
| <span style="background-color:orange"> "10"  </span> | View | This option allows you to view the product in the Visualizer which is very similar to the Catalog Ui and allows  |

<br></br>
Below is the Visualizer that open up when you click on the View button on the Orders page. This visualizer is very similar to our EarthPlatform Ui and has many common components needed to interact with teh Mosaic product similar to our other products


![Visualizer](../Images/EarthMosaics%20UI/Visualizer.png)

That is it !! Happy Mosaicking !! :smile: