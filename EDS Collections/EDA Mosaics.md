# AI Ready Mosaic Creation Parameters

EDA's AI-Ready Mosaics (ARMs) are produced using propretary algorithms to create cloud free temporally coherent images ready for machine learning algorithms or mapping activities. The customization of sources, location, time, and method allow for a mosaic suited for specific analysis purpose being conducted. 

ARM mosaics are produced with 6 bands from the two possible input sources:

|ARM Band Name|Sentinel-2 A/B Band|Landsat 8/9 Band|Approximate Center Wavelength (μ)|
|--|--|--|--|
|Blue|Band 2 - Blue|Band 2 - Blue|0.490
|Green|Band 3 - Green|Band 3 - Green|0.560
|RED|Band 4 - Red|Band 4 - Red|0.665
|NIR08|Band 8A - NIR|Band 5 - NIR|0.865
|SWIR16|Band 11 - SWIR|Band 6 - SWIR 1|1.610
|SWIR22|Band 12 - SWIR|Band 7 - SWIR 2|2.190


## Area of Interest (AOI)

Defines specific geography used to build the mosaic and is a key component for mosaic generation price.

## Time of Interest (TOI)

The time of interest will dictate the amount of available data the mosaic system can draw from. Limiting the TOI can deliver poor results if there is no cloud-free data within the specific AOI and TOI

## Mosaic Settings

### Resolution Selection

#### Preview Mosaic
The preview mosaic is used to ensure the combination of data source, AOI, and TOI is going to be viable for a given mosaic region. It will allow you to see the likely results from a full resolution effort, but at a vastly reduceds resolution. Once the parametesr are to your liking a full resolution mosaic should be produced.

#### Full Resolution
This is the setting to use for a fully capable mosaic product, note this will have a price associated with it and may still produce clouds if the settings for input data are too narrow.  It is advised you preview any mosaic first in order to ensure usability.


## Pixel Selection

#### Best Measurement
ARM's 'Best Measurment' extends work by [White et. al (2014)](#reference) and include pixel-by-pixel weighting for several factors such as: sensor platform, scene content (clear, cloud, cloud shadow, water, snow), and spatial distancing from measurement contamination. This algorithm can produce highly consistent results where the goal is to just choose the most repreesntative sample for a given time period.

#### Peak Normalized Difference Vegetation Index
ARM's 'Peak NDVI' seeks to maximize the vegetative signals from the mosaic process, targeting conditions with the most vigerous vegetation signal. 

#### Peak Burn Severity
ARM's 'Peak Burn Severity' seeks to maximize the response from burned pixels in order to map fire extent and degree of burn over large vegetated regions. This mode can be sensative to date selection and should be informed by knowledge of the local fire conditions and timing.

#### Percentile
ARM's Percentile selection uses a purely statistical approach to identify common pixels from the stack of images, this approach can be very effective with larger volumes of data, from time ranges. 

## Source

## Reference
[White, J. C., Wulder, M. A., Hobart, G. W., Luther, J. E., Hermosilla, T., Griffiths, P., Coops, N. C., Hall, R. J., Hostert, P., Dyk, A., & Guindon, L. (2014). Pixel-Based Image Compositing for Large-Area Dense Time Series Applications and Science. In Canadian Journal of Remote Sensing (Vol. 40, Issue 3, pp. 192–212). Informa UK Limited.](https://doi.org/10.1080/07038992.2014.945827)

