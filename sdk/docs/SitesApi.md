# aqualink_sdk.SitesApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_controller_add_exclusion_dates**](SitesApi.md#sites_controller_add_exclusion_dates) | **POST** /sites/{siteId}/exclusion_dates | Adds exclusion dates to spotter&#39;s data
[**sites_controller_create**](SitesApi.md#sites_controller_create) | **POST** /sites | Creates a new site and its site application
[**sites_controller_delete**](SitesApi.md#sites_controller_delete) | **DELETE** /sites/{siteId} | Deletes specified site
[**sites_controller_deploy_spotter**](SitesApi.md#sites_controller_deploy_spotter) | **POST** /sites/{siteId}/deploy | Deploys site&#39;s spotter
[**sites_controller_find**](SitesApi.md#sites_controller_find) | **GET** /sites | Returns sites filtered by provided filters
[**sites_controller_find_daily_data**](SitesApi.md#sites_controller_find_daily_data) | **GET** /sites/{id}/daily_data | Returns daily data for the specified site
[**sites_controller_find_exclusion_dates**](SitesApi.md#sites_controller_find_exclusion_dates) | **GET** /sites/{siteId}/exclusion_dates | Returns exclusion dates of specified site&#39;s spotter
[**sites_controller_find_latest_data**](SitesApi.md#sites_controller_find_latest_data) | **GET** /sites/{id}/latest_data | Returns latest data for the specified site
[**sites_controller_find_live_data**](SitesApi.md#sites_controller_find_live_data) | **GET** /sites/{id}/live_data | Returns live data for the specified site
[**sites_controller_find_one**](SitesApi.md#sites_controller_find_one) | **GET** /sites/{id} | Returns specified site
[**sites_controller_get_spotter_data**](SitesApi.md#sites_controller_get_spotter_data) | **GET** /sites/{id}/spotter_data | Returns spotter data for the specified site
[**sites_controller_update**](SitesApi.md#sites_controller_update) | **PUT** /sites/{siteId} | Updates specified site


# **sites_controller_add_exclusion_dates**
> sites_controller_add_exclusion_dates(site_id, exclude_spotter_dates_dto)

Adds exclusion dates to spotter's data

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.exclude_spotter_dates_dto import ExcludeSpotterDatesDto
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = aqualink_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    site_id = 1 # float | 
    exclude_spotter_dates_dto = ExcludeSpotterDatesDto(
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # ExcludeSpotterDatesDto | 

    # example passing only required values which don't have defaults set
    try:
        # Adds exclusion dates to spotter's data
        api_instance.sites_controller_add_exclusion_dates(site_id, exclude_spotter_dates_dto)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_add_exclusion_dates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **exclude_spotter_dates_dto** | [**ExcludeSpotterDatesDto**](ExcludeSpotterDatesDto.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Site has no spotter or start date is larger than end date |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_create**
> SiteApplication sites_controller_create(inline_object1)

Creates a new site and its site application

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.site_application import SiteApplication
from aqualink_sdk.model.inline_object1 import InlineObject1
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = aqualink_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    inline_object1 = InlineObject1(
        site=CreateSiteDto(
            name="Duxbury Site",
            latitude=13.21651,
            longitude=132.51651,
            depth=15,
        ),
        site_application=CreateSiteApplicationDto(
            permit_requirements="Some permit requirements",
            funding_source="Some funding source",
            installation_resources="Some installation resources",
            installation_schedule=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new site and its site application
        api_response = api_instance.sites_controller_create(inline_object1)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

[**SiteApplication**](SiteApplication.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_delete**
> sites_controller_delete(site_id)

Deletes specified site

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = aqualink_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    site_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes specified site
        api_instance.sites_controller_delete(site_id)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_deploy_spotter**
> sites_controller_deploy_spotter(site_id, deploy_spotter_dto)

Deploys site's spotter

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.deploy_spotter_dto import DeploySpotterDto
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = aqualink_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    site_id = 1 # float | 
    deploy_spotter_dto = DeploySpotterDto(
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # DeploySpotterDto | 

    # example passing only required values which don't have defaults set
    try:
        # Deploys site's spotter
        api_instance.sites_controller_deploy_spotter(site_id, deploy_spotter_dto)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_deploy_spotter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **deploy_spotter_dto** | [**DeploySpotterDto**](DeploySpotterDto.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Site has no spotter or spotter is already deployed |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find**
> [Site] sites_controller_find()

Returns sites filtered by provided filters

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.site import Site
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    name = "Duxbury Site" # str |  (optional)
    region_id = 1 # float |  (optional)
    admin_id = 1 # float |  (optional)
    status = "in_review" # str |  (optional)
    has_spotter = "hasSpotter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns sites filtered by provided filters
        api_response = api_instance.sites_controller_find(name=name, region_id=region_id, admin_id=admin_id, status=status, has_spotter=has_spotter)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]
 **region_id** | **float**|  | [optional]
 **admin_id** | **float**|  | [optional]
 **status** | **str**|  | [optional]
 **has_spotter** | **str**|  | [optional]

### Return type

[**[Site]**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_daily_data**
> [DailyData] sites_controller_find_daily_data(id, start, end)

Returns daily data for the specified site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.daily_data import DailyData
from aqualink_sdk.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    id = 1 # float | 
    start = "2021-04-18T08:45:35.780Z" # str | 
    end = "2021-05-18T08:45:35.780Z" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns daily data for the specified site
        api_response = api_instance.sites_controller_find_daily_data(id, start, end)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_find_daily_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **start** | **str**|  |
 **end** | **str**|  |

### Return type

[**[DailyData]**](DailyData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Start or end is not a valid date |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_exclusion_dates**
> [ExclusionDates] sites_controller_find_exclusion_dates(site_id)

Returns exclusion dates of specified site's spotter

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.exclusion_dates import ExclusionDates
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = aqualink_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    site_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns exclusion dates of specified site's spotter
        api_response = api_instance.sites_controller_find_exclusion_dates(site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_find_exclusion_dates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |

### Return type

[**[ExclusionDates]**](ExclusionDates.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_latest_data**
> SofarLatestDataDto sites_controller_find_latest_data(id)

Returns latest data for the specified site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.sofar_latest_data_dto import SofarLatestDataDto
from aqualink_sdk.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns latest data for the specified site
        api_response = api_instance.sites_controller_find_latest_data(id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_find_latest_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |

### Return type

[**SofarLatestDataDto**](SofarLatestDataDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_live_data**
> SofarLiveDataDto sites_controller_find_live_data(id)

Returns live data for the specified site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.sofar_live_data_dto import SofarLiveDataDto
from aqualink_sdk.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns live data for the specified site
        api_response = api_instance.sites_controller_find_live_data(id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_find_live_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |

### Return type

[**SofarLiveDataDto**](SofarLiveDataDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_one**
> Site sites_controller_find_one(id)

Returns specified site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.site import Site
from aqualink_sdk.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns specified site
        api_response = api_instance.sites_controller_find_one(id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_find_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_get_spotter_data**
> SpotterDataDto sites_controller_get_spotter_data(id, start_date, end_date)

Returns spotter data for the specified site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.spotter_data_dto import SpotterDataDto
from aqualink_sdk.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    id = 1 # float | 
    start_date = "2021-04-18T08:45:35.780Z" # str | 
    end_date = "2021-05-18T08:45:35.780Z" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns spotter data for the specified site
        api_response = api_instance.sites_controller_get_spotter_data(id, start_date, end_date)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_get_spotter_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **start_date** | **str**|  |
 **end_date** | **str**|  |

### Return type

[**SpotterDataDto**](SpotterDataDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site was found or found site had no spotter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_update**
> Site sites_controller_update(site_id, update_site_dto)

Updates specified site

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api
from aqualink_sdk.model.site import Site
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.update_site_dto import UpdateSiteDto
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = aqualink_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sites_api.SitesApi(api_client)
    site_id = 1 # float | 
    update_site_dto = UpdateSiteDto(
        name="Duxbury Site",
        depth=81,
        region_id=1,
        admin_ids=[1,2,3],
        stream_id=1,
        coordinates=Coordinates(
            latitude=15.5416,
            longitude=-1.456,
        ),
        video_stream="video_stream_example",
    ) # UpdateSiteDto | 

    # example passing only required values which don't have defaults set
    try:
        # Updates specified site
        api_response = api_instance.sites_controller_update(site_id, update_site_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitesApi->sites_controller_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **update_site_dto** | [**UpdateSiteDto**](UpdateSiteDto.md)|  |

### Return type

[**Site**](Site.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

