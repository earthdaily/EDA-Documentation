---
layout: default
title: EDA STAC Extension
parent: STAC Specification
nav_order: 1
---
# View EDA Data Coverage Specification
* Title: EDA Data Coverage Extension
* Identifier: [https://earthdaily-stac-extensions.s3.amazonaws.com/eda_data_coverage/v1.0.0/schema.json](https://earthdaily-stac-extensions.s3.amazonaws.com/eda_data_coverage/v1.0.0/schema.json) 
* Field Name Prefix: eda_data_coverage
* Scope: Item
* History: Prior to March 21, 2024

This document explains the EDA Data Coverage Extension to the [SpatioTemporal Asset Catalog (STAC)](https://github.com/radiantearth/stac-spec) specification.

EDA Data Coverage extension is to define properties for the Data Coverage Reports.

## Fields
*** 
The fields in the table below can be used in these parts of STAC documents:

 - [] Catalogs
 - [] Collections
 - [x] Items
 - [] Assets (for both Collections and Items, incl. Item Asset Definitions in Collections)
 - [] Links

 |  Field Name           | Type        |     Description                                                                        |
 |-----------------------|-------------|----------------------------------------------------------------------------------------|
 | eda_data_coverage:region_id| String      | We divided the entire world into six regions for automated reports, while users can also specify custom regions for manual reports.                                  |
 | eda_data_coverage:item_count     | Number | The number of items considered for this report.                                             |
 | eda_data_coverage:report_type| String      | The frequency of report generation: daily, weekly, or monthly. If the report is manually triggered, the value is custom.                                  |
 | eda_data_coverage:region_version     | Number | If we update the existing regions, we maintain versions here  |
 | eda_data_coverage:month| Number      | Data Coverage Report Month                                 |
 | eda_data_coverage:week| Number      | Data Coverage Report Week                                   |
 
 
 

