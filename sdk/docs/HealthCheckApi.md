# aqualink_sdk.HealthCheckApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_controller_health_check**](HealthCheckApi.md#health_check_controller_health_check) | **GET** /health-check | Checks if the backend is up and running.


# **health_check_controller_health_check**
> health_check_controller_health_check()

Checks if the backend is up and running.

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import health_check_api
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_check_api.HealthCheckApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Checks if the backend is up and running.
        api_instance.health_check_controller_health_check()
    except aqualink_sdk.ApiException as e:
        print("Exception when calling HealthCheckApi->health_check_controller_health_check: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

