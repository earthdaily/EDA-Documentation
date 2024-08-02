# View EDA Extension Specification
* Title: EDA Extension
* Identifier: [https://earthdaily-stac-extensions.s3.amazonaws.com/eda/v0.1.0/schema.json](https://earthdaily-stac-extensions.s3.amazonaws.com/eda/v0.1.0/schema.json) 
* Field Name Prefix: eda
* Scope: Item, Collections
* History: Prior to March 07, 2024

This document explains the EDA Extension to the [SpatioTemporal Asset Catalog (STAC)](https://github.com/radiantearth/stac-spec) specification.

EDA Extension adds metadata related to EDA specific details like ImagerMode, Sensor Type, Water Cover, Radiometric Scaling, Geometric Accuracy RMSE etc  that affect the view of resulting data. It will often be combined with other extensions that describe the actual data, such as the eo, proj or sat extensions.

## Fields
*** 
The fields in the table below can be used in these parts of STAC documents:

 - [] Catalogs
 - [x] Collections
 - [x] Items
 - [] Assets (for both Collections and Items, incl. Item Asset Definitions in Collections)
 - [] Links

Below is the list of **public** fields available via API

 |  Field Name           | Type        |     Description                                                                        |
 |-----------------------|-------------|----------------------------------------------------------------------------------------|
 | eda:order_line_item_id| String      | Specifies the order line item id within EarthPipeline                                  |
 | eda:source_l0_ids     | List of Strings | Archive IDs of the source level-0 datasets                                             |
 | eda:source_l0_scene_ids| List of Strings      | Scene IDs of the source Level-0 datasets                                  |
 | eda:segment_id     | String | Dataset identifier for the acquisition used to generate the product \<Datetime\>\_\<Sensor\>\<SID\>\<Cat\>  |
 | eda:imager_mode| String      | Non-experimental modes are: “TDI_LAND”, “TDI_MARITIME”, “TDI_GLOBAL”, “PUSH_FRAME_GLOBAL” Only provided for the Catalogue products                                  |
 | eda:image_section_counter| Number      | Image section counter. Only provided for the Catalogue products                                   |
 | eda:geometric_accuracy_rmse| Number      | Radial RMSE, in meters. Only provided for the following products: L1C VNIR Land TOA, VNIR RGB Visually Enhanced, VNIR NRG Visually Enhanced, L1C SWIR Land TOA, L1C LWIR Brightness Temperature, L1C MWIR Brightness Temperature, L2A VNIR Basic Land BOA, L2A VNIR Advanced Land BOA, L2A SWIR Land BOA, L2A LWIR Land Surface Temperature                                 |
 | eda:sensor_type| String      | The sensor type right now is "OPTICAL" but we might have different values depending on product type like Methane or thermal products                                  |
 | eda:product_type     | String | Only available for the "GOES" collection                                            |
 | eda:water_cover| Number      | Estimate of water cover, in %
 | eda:derived_from_item_id| String      | L2 item that was used for the creation of the L2 derived products             |
 | eda:derived_from_collection_id     | String | L2 collection that was used for the creation of the L2 derived products                                              |
 | eda:ag_cloud_mask_available| Boolean      | Specifies whether EDAgro cloud mask is available or not                                  |
 | eda:ag_cloud_mask_item_id| String      | EDAgro Cloud Mask item id available for this item                                  |
 | eda:ag_cloud_mask_collection_id| String      | EDAgro Cloud Mask collection id available for this item                                   |
 | eda:cloud_mask_available | Boolean      | Specifies whether EDA cloud mask is available or not                                  |
 | eda:cloud_mask_item_id | String      | EDA Cloud Mask item id available for this item                                  |
 | eda:cloud_mask_collection_id | String      | EDA Cloud Mask collection id available for this item  |
 | eda:area_km2     | Number |   Mosaic - the approximate area in km^2 of the valid region of the mosaic                                           |
 | eda:radiometric_scaling| Number      |   Obsolete                                |
 | eda:orbit_number| String      |    The satellite orbit                               |
 | eda:pixel_composite_method| String      |    Pixel Composite Method used for Mosaics                               |

 Below are some of the **private** fields being available
 
 **Note** The private fields are available to "Admin users" and "All Users of Customer account with Super Tier"

 |  Field Name           | Type        |     Description                                                                        |
 |-----------------------|-------------|----------------------------------------------------------------------------------------|
 | eda:status| String      | Status of the product. Can take one of the following values - Created, Published,Unpublished                                 |
 | eda:geometry_tags     | List of Strings | This field is populated when we modify the STAC items from third party data                                 |
 | eda:tags| List of Strings      | General EDA tags                                  |
 | eda:original_geometry     | Object | We preserve the original geometry when we modify the geometry tags of third party STAC items  |
 | eda:tracking_id| String      | Used by Pastfinder for tracking all items related to an order                                  |
 | eda:account_id| String      | User account id info (Customer Account Id) used for authorization and product delivery                                   |
 | eda:processor_version| String      | Version of the processing system used to generate this product                                 |
 | eda:loose_validation_status| String      | Validation status of third party stac items because even if its not valid, we would store it and display it as well (queryable)                                  |
 | eda:band_to_band_accuracy_rmse     | List of Objects | The band-to-band accuracy, in pixels. Only provided for the following products: L1C VNIR Land TOA, VNIR RGB Visually Enhanced, VNIR NRG Visually Enhanced, L1C SWIR Land TOA, L1C LWIR Brightness Temperature, L2A VNIR Basic Land BOA, L2A VNIR Advanced Land BOA, L2A SWIR Land BOA, L2A LWIR Land Surface Temperature                                            |
 | eda:source_created| String      | If we ingest third party item, we keep a track of when it was created in our system but we also maintain history of the actual item created. This is when third party created it
 | eda:source_updated| String      | If we ingest third party item, we keep a track of when it was updated in our system but we also maintain history of the actual item updated. This is when third party updated it             |
 | eda:unusable_cover     | Number | Estimate of unusable cover. Only for Land products. Unusable cover includes at least cloud and water.            |
 | eda:num_cols| String      |                                   |
 | eda:num_rows| String      |                                  |
 | eda:derived_from_l1c_item_id| String      | Which L1c item was used for the creation of the L1 derived products                                  |
 | eda:derived_from_l1c_collection_id     | String | Which L1c collection was used for the creation of the L1 derived collection                   |
 | eda:altitude| Number      |   Altitude of the image capture location. Altitude at the center of the product                                |
 | eda:bearing|  Number      |    Satellite ground track bearing                               |
 | eda:start_attitude| List of Numbers      |   Satellite attitude at the start of the acquisition (Degrees RPY )                                |
 | eda:end_attitude| List of Numbers      |    Satellite attitude at the end of the acquisition (Degrees RPY )                               |
 | eda:mean_attitude| List of Numbers      |   Mean satellite attitude (Degrees RPY )                                |
 | eda:mtf_enhancement_applied| Boolean      |   Indicates whether MTF enhancement was applied                                |
 | eda:product_status| Number      |   Mosaic Product Status - Pending Validation, Valid, Deprecated . Obsolete                              |
 | eda:source| String      |     Obsolete                              |
 | eda:auxiliary_atmospheric_sources| Object      |   Auxiliary atmospheric retrieval sources that were used for BOA generation (empty if none were used) Only applicable and included for L2A VNIR Basic Land BOA and L2A VNIR Advanced Land BOA products. e.g. `{ “aerosol”: “MODIS”, “water_vapour”: “ECMWF observation”}`
 | eda:basemap| String      |  The geometric reference used for any geometric corrections applied to the imagery  (Mosaic)                                |
 | eda:download_bundle_status| Number      |   Whether the download bundle asset is available or in progress. If this tag is absent, then the download bundle asset is not available for that item.|
 | eda:aocs_mode| String      |   AOCS Mode - One of “Nadir”, “DEM”, “Side Slither”.  Only provided for the Catalogue                                |
 | eda:cloud_detect_method| String | Algorithm used in cloud detection |