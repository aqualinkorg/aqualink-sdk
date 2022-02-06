# aqualink_sdk.HealthCheckApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_controller_health_check**](HealthCheckApi.md#health_check_controller_health_check) | **GET** /health-check | Checks if the backend is up and running.

# **health_check_controller_health_check**
> health_check_controller_health_check()

Checks if the backend is up and running.

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aqualink_sdk.HealthCheckApi()

try:
    # Checks if the backend is up and running.
    api_instance.health_check_controller_health_check()
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

