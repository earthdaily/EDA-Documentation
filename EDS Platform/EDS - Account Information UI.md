# Table of Contents
* [Introduction](#introduction)
* [My Account](#my-account)
* [My Orders](#my-orders)
* [My Subscriptions](#my-subscriptions)
* [My Subscription Areas](#my-subscription-areas)

## Introduction
The Account Information page is the landing page for each user of the customer account when they login to the [Account Information](https://earthplatform.eds.earthdaily.com/am) It allows the user to check his own account details, his orders , his subscriptions etc. It also has the link to the other applications like Catalog UI, Mosaic etc

<br></br>

## My Account
| S. No | Label | Description |
|-------|-------|-------------|
| <span style="background-color:orange"> " 1 "  </span>     | User   |  Logged in user details |
| <span style="background-color:orange"> " 2 "  </span>     | Account | Details of the account that the user belongs to. |
| <span style="background-color:orange"> " 3 "  </span>     | API Credentials |  Token URL to generate “Bearer Token” for API authentication. |
| <span style="background-color:orange"> " 4 "  </span>     | Hosted Apps     | Use this to switch between various apps available. |

<br></br>


![My Account](../Images/Account%20UI/Account%20Information.png)

## My Orders

It lists all the orders being placed under the customer account you belong to. The purpose of showing all the orders apart from the one you placed is mainly for optimization, to ensure that you don’t end up placing a duplicate order.


|  S.No &nbsp     | Label | Description |
|---------|-------|-------------|
| <span style="background-color:orange"> " 5 " </span>     | My Orders | To go to your orders page. |
|<span style="background-color:orange"> " 6 "  </span>     | Search by Id | If you know your Orders Id, you can use this to search your order. |
|<span style="background-color:orange"> " 7 "  </span>    | Order Details dropdown | This dropdown shows all the details related to your order. Once order is placed, you will see it in “Processing” state. When the order is completed, it will show “Processed“ and you will also have the Processed date and time for that oder. The Product UUID will also show up after order is processed. This can be helpful to use for searching your product in destination bucket or troubleshooting.
|<span style="background-color:orange"> " 8 "  </span>    | Search | This is a free form text search similar to browser search for anything in the results. Instead of searching on the current page (like browser search), this is quite helpful when you want to do free form search on the whole result. It also filters the result records based on the match.|
|<span style="background-color:orange"> " 9 "  </span>    | Download | It allows you to download the search results as a csv if you want to to further analyze and do advanced queries. It only extracts the first level order records and leaves out the dropdown order details. |
| <span style="background-color:orange"> " 10 "  </span>   | Print | Allows you to print the search results. |
|<span style="background-color:orange"> " 11 "  </span>    | View Columns | Allows you to select the columns you want to view for the search results |
|<span style="background-color:orange"> " 12 "  </span>   | Filter | This is the detailed filter for every attribute of the order and allows you to select from the values in all the orders. |
|<span style="background-color:orange"> " 13 "  </span>   | Refresh | Refreshes the page as per current criteria. |

 <br></br>


![My Orders](../Images/Account%20UI/My%20Orders.png)

<br></br>

## My Subscriptions

Shows you a list of subscriptions that you created

| S. No | Label | Description |
|-------|-------|-------------|
| <span style="background-color:orange"> " 14 "  </span> | Results Criteria |  Various parameters for the search results |
| <span style="background-color:orange"> " 15 "  </span> | List View | Allows to show the results in the list view as seen below |
| <span style="background-color:orange"> " 16 "  </span> | Map View | Allows to show the subscriptions in the map for better clarity |
| <span style="background-color:orange"> " 17 "  </span> | View AoI on Map | To view the selected AoI in Map View |
| <span style="background-color:orange"> " 18 "  </span> | Display all metadata | Clicking this button will bring up a form with subscription details |
<br></br>

![My Subscriptions](../Images/Account%20UI/My%20Subscriptions.png)

Clicking the metadata button in the list view shows the subscription details as below


![My Subscription MetaData](../Images/Account%20UI/My%20Subscription%20Metadata.png)
 
<br></br>
Below is the Map view of the all the subscriptions on the map. You can click the center mass of the subscription area to see the metadata as shown below.

![My Subscription Map](../Images/Account%20UI/My%20Subscription%20Map.png)


## My Subscription Areas

Shows you a list of subscription areas that you created. The screen for Subscription areas is very similar to the subscription in the way you interact with the data as seen below.
<br></br>

![My Subscription Areas](../Images/Account%20UI/My%20Subscription%20Areas.png)

