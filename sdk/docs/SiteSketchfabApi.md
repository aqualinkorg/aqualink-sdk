# aqualink_sdk.SiteSketchfabApi

All URIs are relative to *https://production-dot-ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**site_sketch_fab_controller_find**](SiteSketchfabApi.md#site_sketch_fab_controller_find) | **GET** /site-sketchfab | 


# **site_sketch_fab_controller_find**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} site_sketch_fab_controller_find(site_id)



### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import site_sketchfab_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = site_sketchfab_api.SiteSketchfabApi(api_client)
    site_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.site_sketch_fab_controller_find(site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SiteSketchfabApi->site_sketch_fab_controller_find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

