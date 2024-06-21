# Authentication


EarthPlatform STAC API is protected by bearer authentication.
A bearer token must be generated using [OAuth Client Credentials Flow](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/). The required client_id, client_secret and access_token_url values can be found on [Account Management](https://earthplatform.eds.earthdaily.com/am) page. These API credentials are specific to your user account on EarthPlatform and should be kept confidential.

![Client Credentials](../Images/STAC%20API//Account%20Information.png)

Example curl request to generate token



```
curl --location '<ACCESS_TOKEN_URL HERE>'  
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=<CLIENT_ID HERE>' \ 
--data-urlencode 'client_secret=<CLIENT SECRET HERE>' \
--data-urlencode 'grant_type=client_credentials'
```

Example curl response

```
{"access_token":"eyJraWQiO.......","expires_in":3600,"token_type":"Bearer"}
```

* The generated access_token will have a 1 hour expiry. 
* The access token should be cached locally and included in each STAC API request as a bearer authorization header.  
* When the access token has expired, an error 401 (Unauthorized) will be returned from STAC API requests. 