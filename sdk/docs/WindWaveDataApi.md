# aqualink_sdk.WindWaveDataApi

All URIs are relative to *https://production-dot-ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wind_wave_controller_get_wind_wave_data**](WindWaveDataApi.md#wind_wave_controller_get_wind_wave_data) | **GET** /wind-wave-data-hindcast/sites/{siteId} | Return hindcast wind and wave date for a specified site


# **wind_wave_controller_get_wind_wave_data**
> wind_wave_controller_get_wind_wave_data(site_id)

Return hindcast wind and wave date for a specified site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import wind_wave_data_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = wind_wave_data_api.WindWaveDataApi(api_client)
    site_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Return hindcast wind and wave date for a specified site
        api_instance.wind_wave_controller_get_wind_wave_data(site_id)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling WindWaveDataApi->wind_wave_controller_get_wind_wave_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

