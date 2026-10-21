# aqualink_sdk.SensorDataApi

All URIs are relative to *https://production-dot-ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensor_data_controller_find_sensors**](SensorDataApi.md#sensor_data_controller_find_sensors) | **GET** /sensor-data | Get sofar data by sensorId
[**sensor_data_controller_sensor_info**](SensorDataApi.md#sensor_data_controller_sensor_info) | **GET** /sensor-data/info | Get sensor status information


# **sensor_data_controller_find_sensors**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sensor_data_controller_find_sensors(id, start, end)

Get sofar data by sensorId

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sensor_data_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sensor_data_api.SensorDataApi(api_client)
    id = "SPOT-0000" # str | 
    start = "2022-05-27" # str | 
    end = "2022-05-28" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get sofar data by sensorId
        api_response = api_instance.sensor_data_controller_find_sensors(id, start, end)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SensorDataApi->sensor_data_controller_find_sensors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **start** | **str**|  |
 **end** | **str**|  |

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

# **sensor_data_controller_sensor_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sensor_data_controller_sensor_info(site_id, sensor_id)

Get sensor status information

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import sensor_data_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
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
    api_instance = sensor_data_api.SensorDataApi(api_client)
    site_id = 1063 # float | 
    sensor_id = "SPOT-0000" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get sensor status information
        api_response = api_instance.sensor_data_controller_sensor_info(site_id, sensor_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SensorDataApi->sensor_data_controller_sensor_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **sensor_id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

