# Temporally Consistent AI-Ready Mosaics

Powering ML applications with a seamless cloud-free image 

# What Are AI-Ready Mosaics
AI-Ready mosaics leverage advanced processing 

## STAC Item Structure
[TBW]

## Methods
### Cloud Masking

[EDA's Accurate Cloud Masking](https://earthdailyagro.com/spend-less-data-scientists-time-cleaning-data-high-quality-cloud-masks-for-sentinel2-landsat-and-others-available-today/) have been shown to be more accurate then current open data standard processing which improves ML applications and the pixel compositing process for mosaics. 

The accuracy of the EarhDaily Agro cloud mask is higher than the cloud mask of other providers, allowing for a reduction in under-detection and keeping a high quality on cloud over-detection to not miss clear areas. 

|Cloud Mask Provider|Over-Detection|Under-Detection|
|:----:|:----:|:----:|
ACM|1.65%|3.85%
Fmask 4 (Matlab)|0.21%|27.18%
Fmask (Python)|1.12%|26.6%
ESA|0.97%|42.1%


EDA's Auto Clear Mask (ACM) improves the detection and the efficeny of clouds in Senintel-2, Landsat 8, and Landsat 9.

|<p style="text-align: center;">Mosaics Produced with ESA's Cloud Mask</p> | <p style="text-align: center;">Mosaics Produced with EDA's Cloud Masks</p>|
|:---:|:----:|
|<img src="../Images/Product Images/Base Cloud Mask Mosaic.png" width=100% height=500> | <img src="../Images/Product Images/EDA Cloud Mask Mosaic.png" width=100% height=500>|


### Pixel Composition
EDA's AI-Ready Mosaics employ a customer 'Best Measurment' algorithm by extending the work by [White et. al (2014)](#reference)

This includes pixel-by-pixel weighting for several factors such as: sensor platform, scene content (clear, cloud, cloud shadow, water, snow), and spatial distancing from measurement contamination.

### Reference
[White, J. C., Wulder, M. A., Hobart, G. W., Luther, J. E., Hermosilla, T., Griffiths, P., Coops, N. C., Hall, R. J., Hostert, P., Dyk, A., & Guindon, L. (2014). Pixel-Based Image Compositing for Large-Area Dense Time Series Applications and Science. In Canadian Journal of Remote Sensing (Vol. 40, Issue 3, pp. 192–212). Informa UK Limited.](https://doi.org/10.1080/07038992.2014.945827)


# Custom Orders
Mosaics that are available outside of the self-serve interface, please contact EDA for more customization to your buisness needs.