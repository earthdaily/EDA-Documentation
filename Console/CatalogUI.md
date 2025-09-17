---
layout: default
title: EarthPlatform
grand_parent: EDS Documentation
parent: Console
nav_order: 3
---

# Table of Contents
* [Introduction](#introduction)
* [Search](#search)
* [Interacting with the catalog data](#interacting-with-the-catalog)

<!--
* [Interacting with the product data](#interacting-with-the-product) 
* [Placing an order and receiving it](#placing-an-order-and-receiving-it)
-->

## Introduction
Customers can access and browse through our image catalog and products through the EarthPlatform. In addition to providing useful metadata and details about the listed images, it provides capabilities to interact with them. You can access the EarthPlatform [here](https://console.earthdaily.com/platform).


## Search
EarthPlatform has a search panel with various customization options. Let's have a look at them.

Once you login with your credentials, the landing page for EarthPlatform is shown. On the left hand side, you can find the search filters and search results panel:

| S. No     | Label     | Description       |
|-----------|-----------|-------------------|
| ![One](../Images/NumberLabels/One.png) | Search Box | Enter any geographic area like “Vancouver”, “Chile” etc to find and focus. |
| ![Two](../Images/NumberLabels/Two.png) | Rectangle Tool | Select two vertices of the diagonal on the map to form a rectangular area as a geospatial filter. |
| ![Three](../Images/NumberLabels/Three.png)  | Polygon Tool | Select a given area as a geospatial filter on the map by creating a vertex as and when you do a left click. Make sure you click the first vertex of the polygon or double-click after creating the last vertex to complete it. |
| ![Four](../Images/NumberLabels/Four.png) | Input GeoJSON | Click this button if you have a GeoJson you wish to enter or import as a geospatial filter. |
| ![Five](../Images/NumberLabels/Five.png) | Viewport | Select this to define the current map extents as a geospatial filter. |
| ![Six](../Images/NumberLabels/Six.png) | Basic Filters | Select one or more Collections (up to 15) from the list and define a date range as your basic search filters.|
| ![Seven](../Images/NumberLabels/Seven.png) | Advanced Filters | Click on the Advanced Filters icon to define additional filters based on the Collections selected. |
| ![Eight](../Images/NumberLabels/Eight.png)| Reset Button | Click to reset all search filters. |
| ![Nine](../Images/NumberLabels/Nine.png)| Search Button | Click to submit the search. |
| ![Ten](../Images/NumberLabels/Ten.png) | Results Panel | This is the area where you would see the thumbnails of the search results for your images. |


![EarthPlatform Landing Page - Search Filters and Results](../Images/CatalogUI/LandingPageFilters.png)

NOTE : The Advanced Filters panel expands with additional parameters based on the Collection selected, as shown below. When there are results returned from the search, you can see the results panel populated with images, along with thumbnails if available. When you hover over a search result, the corresponding footprint will be highlighted in yellow on the map.

![EarthPlatform Filter Panel](../Images/CatalogUI/Filter.png)

On the right hand side is the map, where you can define the Area of Interest (AOI) and see the footprints of the search results:

| S. No     | Label     | Description       |
|-----------|-----------|-------------------|
| ![Eleven](../Images/NumberLabels/Eleven.png) | App Switcher | Click this button to switch to another EDA-hosted application. |
| ![Twelve](../Images/NumberLabels/Twelve.png) | Map Slider | Click to enable the Map Slider to enter the image comparison mode. |
| ![Thirteen](../Images/NumberLabels/Thirteen.png) | Settings | Click to change base map layers, map projection, and units. |
| ![Fourteen](../Images/NumberLabels/Fourteen.png) | Ruler | Click to draw a line and measure the distance between 2 points. |
| ![Fifteen](../Images/NumberLabels/Fifteen.png) | Help Center | Click to report an issue, contact us, or access the documentation. |
| ![Sixteen](../Images/NumberLabels/Sixteen.png)| Bottom Panel | Shows latitude and longitude of current cursor position, current map zoom level, and the map scale bar. |

![EarthPlatform Landing Page - Map](../Images/CatalogUI/LandingPageMap.png)

Below are some images that will give you an idea of how the various controls work.

![EarthPlatform Polygon Area Calculator](../Images/CatalogUI/AreaCalculator.png)

![EarthPlatform Rectangular Area Calculator](../Images/CatalogUI/AreaCalculatorSqr.png)


GeoJSON Viewer and Importer

![EarthPlatform JSON Viewer](../Images/CatalogUI/JSONViewer.png)


Streets and Satellite Views

 | Streets View  |   Satellite & Streets View  |
 |--------------|-------------------|
 |![StreetView](../Images/CatalogUI/StreetView.png)| ![SatelliteView](../Images/CatalogUI/SatelliteView.png) |


Ruler

![EarthPlatform Ruler](../Images/CatalogUI/Ruler.png)


## Interacting with the catalog

Now let's see once you have the search results, what you can do with those images. As you can see below, you can click different icons to perform actions on them. There is also a small checkbox for you to select multiple items and then perform actions on them.

| S. No.    |  Label    | Description       |
|-----------|-----------|-------------------|
| ![Seventeen](../Images/NumberLabels/Seventeen.png)  | Show Item Properties | Show the Item Properties on the right hand side panel. |
| ![Eighteen](../Images/NumberLabels/Eighteen.png)  | Favorite Item | Tag the image as favorite, and then use the toggle button on top (#26) to show only the items tagged as favorites. |
| ![Nineteen](../Images/NumberLabels/Nineteen.png)  | Fly to Bounds | Zoom in to the image location. |
| ![Twenty](../Images/NumberLabels/Twenty.png)  | Toggle Layer Visibility | Show/Hide the footprint on the map. |
| ![TwentyOne](../Images/NumberLabels/TwentyOne.png)  | View on Map | Render the image on the map. |
| ![TwentyTwo](../Images/NumberLabels/TwentyTwo.png)  | View Visualization Configuration | Toggles the visualization configuration panel where you can adjust the min and max of the available color bands and also the gamma values. You can update the min and max of the current image or optionally update all images from the same Collection. |
| ![TwentyThree](../Images/NumberLabels/TwentyThree.png)  | Auto adjust Visualization | Shorthand convenience tool to auto adjust the image by clipping desired percentages off the image, based on a calculated histogram. If the values in the visualization configuration panel have not been modified then it applies the default values of 2% and 98%. |
| ![TwentyFour](../Images/NumberLabels/TwentyFour.png)  | Multi-Select | Allows you to multi-select images and perform actions on them. See #25 for the action menu. | 
| ![TwentyFive](../Images/NumberLabels/TwentyFive.png)  | Multi-Select Actions | Actions that you can perform on multiple images. The first one 'View all on map' allows you to render all the images on the map. Use this with caution as it takes time to render if you have a large number of images. | 
| ![TwentySix](../Images/NumberLabels/TwentySix.png)  | View Favorites Only | This toggle button will show all the images that the user has tagged as favorite (see #18). |

![EarthPlatform Interaction](../Images/CatalogUI/CatalogInteraction.png)

Below is an example of toggling the Item Properties to be shown on the right. A subset of the STAC item properties will be shown


![EarthPlatform Item Properties](../Images/CatalogUI/ItemProperties.png)


Toggle the Show Full button to show the entire contents of the STAC item properties, as below. Under the Show Full mode you can also get the individual asset urls and download the images by following the "href"

![EarthPlatform Show Full](../Images/CatalogUI/ShowFull.png)

Here is an example of tagging an item as favorite and then toggling the Favorites only button to see only the favorites list

| Favorites  |   View Favorites  |
 |--------------|-------------------|
 |![Favorites](../Images/CatalogUI/Favorites.png)| ![ViewFavorites](../Images/CatalogUI/ViewFavourites.png) |

Next is an example of the View on Map button

![EarthPlatform View on Map](../Images/CatalogUI/MapView.png)

Here is an example of what the visualization configuration options can do when you change the min and the max band ranges

![EarthPlatform Visualization](../Images/CatalogUI/Visualization.png)

Below is an example where two images are selected and viewed on the map. Auto visualization was applied for the right hand side image and you can see the difference it makes

![EarthPlatform Auto Visualization](../Images/CatalogUI/AutoVisualization.png)

Below is an example of flying to the geographic bounds of an image

![EarthPlatform Fly To Bounds](../Images/CatalogUI/FlyToBounds.png)

Next, we can see how we can compare two images over a period of time to see how the landscape is changing. We can do this by using the Map Slider

Below there are two images chosen over the same area but with different dates “2022-12-16“ and “2023-03-22“. They have been tagged as favorite (with view favorite list enabled) and View on Map enabled to be able to see the landscape details.

| S. No.    | Label     | Description       |
|-----------|-----------|-------------------|
| ![TwentySeven](../Images/NumberLabels/TwentySeven.png)  | Show/Hide Map Slider | This is the toggle for Map Slider. It gives you a capability to slide the area from left to right. This is especially useful when you have two images that you want to compare. As you slide you will be able to see the landscape changes given the images are of different dates. |
| ![TwentyEight](../Images/NumberLabels/TwentyEight.png) | Move Image Left | Click this Left button to select the image to be seen on the left of the map slider. | 
| ![TwentyNine](../Images/NumberLabels/TwentyNine.png) | Move Image Right | Click this Right button to select the image to be seen on the right of the map slider. | 
| ![Thirty](../Images/NumberLabels/Thirty.png) | Slider | The map slider.  |


![EarthPlatform Map Slider](../Images/CatalogUI/MapSlider.png)


Below are the differences over another area which shows the installation of the solar panels that happened within the period 2023-10-28 to 2024-01-26

![EarthPlatform Map Slider Left](../Images/CatalogUI/MapSliderLeft.png)

![EarthPlatform Map Slider Right](../Images/CatalogUI/MapSliderRight.png)

Now, there are some slider options to help you adjust the opacity


| S. No.    | Label     | Description       |
|-----------|-----------|-------------------|
| ![ThirtyOne](../Images/NumberLabels/ThirtyOne.png)  | Image Opacity | Image Opacity is used to toggle the opacity/transparency of an image. |
| ![ThirtyTwo](../Images/NumberLabels/ThirtyTwo.png)  | Image Footprint Opacity | Image Footprint Opacity is used to toggle the opactiy/transparency of the footprint of an image. This is useful when you want to see the basemap more clearly, especially when there are multiple footprints overlapping the same area causing the basemap to be difficult to see. |


![EarthPlatform Image Sliders](../Images/CatalogUI/ImageSliders.png)

Below you can see the opacity for the image at 100%, 50% and 0

 | Image Opacity 0  |   Image Opacity 50  |   Image Opacity 100   | 
 |--------------|-------------------|-------------------|
 |![ImageOpacity0](../Images/CatalogUI/ImageOpacity0.png)| ![ImageOpacity50](../Images/CatalogUI/ImageOpacity50.png) |  ![ImageOpacity100](../Images/CatalogUI/ImageOpacity100.png) | 

Here are examples of adjusting the Footprint opacity

 | Footprint Opacity High  |   Footprint Opacity Low  |  
 |--------------|-------------------|
 |![FootprintOpacityHigh](../Images/CatalogUI/FootprintOpacityHigh.png)| ![FootprintOpacityLow](../Images/CatalogUI/FootprintOpacityLow.png) | 


That completes the list of our extensive features that are available in EarthPlatform.

<!-- 
## Interacting with the product
## Placing an order and receiving it
-->
