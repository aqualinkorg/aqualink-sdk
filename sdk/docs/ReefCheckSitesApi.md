# aqualink_sdk.ReefCheckSitesApi

All URIs are relative to *https://production-dot-ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reef_check_sites_controller_find_one**](ReefCheckSitesApi.md#reef_check_sites_controller_find_one) | **GET** /reef-check-sites/{id} | Returns specified reef check site


# **reef_check_sites_controller_find_one**
> reef_check_sites_controller_find_one(id)

Returns specified reef check site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import reef_check_sites_api
from aqualink_sdk.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reef_check_sites_api.ReefCheckSitesApi(api_client)
    id = "12345678-abcd-efgh-12345678" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns specified reef check site
        api_instance.reef_check_sites_controller_find_one(id)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling ReefCheckSitesApi->reef_check_sites_controller_find_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | No reef check site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

