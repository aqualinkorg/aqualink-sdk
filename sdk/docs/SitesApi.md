# swagger_client.SitesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_controller_add_exclusion_dates**](SitesApi.md#sites_controller_add_exclusion_dates) | **POST** /sites/{siteId}/exclusion_dates | Adds exclusion dates to spotter&#x27;s data
[**sites_controller_create**](SitesApi.md#sites_controller_create) | **POST** /sites | Creates a new site and its site application
[**sites_controller_delete**](SitesApi.md#sites_controller_delete) | **DELETE** /sites/{siteId} | Deletes specified site
[**sites_controller_deploy_spotter**](SitesApi.md#sites_controller_deploy_spotter) | **POST** /sites/{siteId}/deploy | Deploys site&#x27;s spotter
[**sites_controller_find**](SitesApi.md#sites_controller_find) | **GET** /sites | Returns sites filtered by provided filters
[**sites_controller_find_daily_data**](SitesApi.md#sites_controller_find_daily_data) | **GET** /sites/{id}/daily_data | Returns daily data of the specified site
[**sites_controller_find_exclusion_dates**](SitesApi.md#sites_controller_find_exclusion_dates) | **GET** /sites/{siteId}/exclusion_dates | Returns exclusion dates of specified site&#x27;s spotter
[**sites_controller_find_live_data**](SitesApi.md#sites_controller_find_live_data) | **GET** /sites/{id}/live_data | Returns live data of the specified site
[**sites_controller_find_one**](SitesApi.md#sites_controller_find_one) | **GET** /sites/{id} | Returns specified site
[**sites_controller_get_spotter_data**](SitesApi.md#sites_controller_get_spotter_data) | **GET** /sites/{id}/spotter_data | Returns spotter data of the specified site
[**sites_controller_update**](SitesApi.md#sites_controller_update) | **PUT** /sites/{siteId} | Updates specified site

# **sites_controller_add_exclusion_dates**
> sites_controller_add_exclusion_dates(body, site_id)

Adds exclusion dates to spotter's data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExcludeSpotterDatesDto() # ExcludeSpotterDatesDto | 
site_id = 1.2 # float | 

try:
    # Adds exclusion dates to spotter's data
    api_instance.sites_controller_add_exclusion_dates(body, site_id)
except ApiException as e:
    print("Exception when calling SitesApi->sites_controller_add_exclusion_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExcludeSpotterDatesDto**](ExcludeSpotterDatesDto.md)|  | 
 **site_id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_create**
> SiteApplication sites_controller_create(body)

Creates a new site and its site application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SitesBody() # SitesBody | 

try:
    # Creates a new site and its site application
    api_response = api_instance.sites_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->sites_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SitesBody**](SitesBody.md)|  | 

### Return type

[**SiteApplication**](SiteApplication.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_delete**
> sites_controller_delete(site_id)

Deletes specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 1.2 # float | 

try:
    # Deletes specified site
    api_instance.sites_controller_delete(site_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_deploy_spotter**
> sites_controller_deploy_spotter(body, site_id)

Deploys site's spotter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeploySpotterDto() # DeploySpotterDto | 
site_id = 1.2 # float | 

try:
    # Deploys site's spotter
    api_instance.sites_controller_deploy_spotter(body, site_id)
except ApiException as e:
    print("Exception when calling SitesApi->sites_controller_deploy_spotter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeploySpotterDto**](DeploySpotterDto.md)|  | 
 **site_id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find**
> list[Site] sites_controller_find(name=name, region_id=region_id, admin_id=admin_id, status=status, has_spotter=has_spotter)

Returns sites filtered by provided filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SitesApi()
name = 'name_example' # str |  (optional)
region_id = 1.2 # float |  (optional)
admin_id = 1.2 # float |  (optional)
status = 'status_example' # str |  (optional)
has_spotter = 'has_spotter_example' # str |  (optional)

try:
    # Returns sites filtered by provided filters
    api_response = api_instance.sites_controller_find(name=name, region_id=region_id, admin_id=admin_id, status=status, has_spotter=has_spotter)
    pprint(api_response)
except ApiException as e:
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

[**list[Site]**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_daily_data**
> list[DailyData] sites_controller_find_daily_data(id, start, end)

Returns daily data of the specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SitesApi()
id = 1.2 # float | 
start = 'start_example' # str | 
end = 'end_example' # str | 

try:
    # Returns daily data of the specified site
    api_response = api_instance.sites_controller_find_daily_data(id, start, end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->sites_controller_find_daily_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **start** | **str**|  | 
 **end** | **str**|  | 

### Return type

[**list[DailyData]**](DailyData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_exclusion_dates**
> list[ExclusionDates] sites_controller_find_exclusion_dates(site_id)

Returns exclusion dates of specified site's spotter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
site_id = 1.2 # float | 

try:
    # Returns exclusion dates of specified site's spotter
    api_response = api_instance.sites_controller_find_exclusion_dates(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->sites_controller_find_exclusion_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  | 

### Return type

[**list[ExclusionDates]**](ExclusionDates.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_live_data**
> SofarLiveDataDto sites_controller_find_live_data(id)

Returns live data of the specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SitesApi()
id = 1.2 # float | 

try:
    # Returns live data of the specified site
    api_response = api_instance.sites_controller_find_live_data(id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_find_one**
> Site sites_controller_find_one(id)

Returns specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SitesApi()
id = 1.2 # float | 

try:
    # Returns specified site
    api_response = api_instance.sites_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_get_spotter_data**
> SpotterDataDto sites_controller_get_spotter_data(id, start_date, end_date)

Returns spotter data of the specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SitesApi()
id = 1.2 # float | 
start_date = 'start_date_example' # str | 
end_date = 'end_date_example' # str | 

try:
    # Returns spotter data of the specified site
    api_response = api_instance.sites_controller_get_spotter_data(id, start_date, end_date)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_controller_update**
> Site sites_controller_update(body, site_id)

Updates specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateSiteDto() # UpdateSiteDto | 
site_id = 1.2 # float | 

try:
    # Updates specified site
    api_response = api_instance.sites_controller_update(body, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->sites_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSiteDto**](UpdateSiteDto.md)|  | 
 **site_id** | **float**|  | 

### Return type

[**Site**](Site.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

