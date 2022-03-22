# aqualink_sdk.SensorsApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensors_controller_find_sensor_data**](SensorsApi.md#sensors_controller_find_sensor_data) | **GET** /sensors/{id}/data | Get data from a specified sensor
[**sensors_controller_find_sensor_surveys**](SensorsApi.md#sensors_controller_find_sensor_surveys) | **GET** /sensors/{id}/surveys | Get surveys and survey media from a specified sensor
[**sensors_controller_find_sensors**](SensorsApi.md#sensors_controller_find_sensors) | **GET** /sensors | Get all sites having sensors


# **sensors_controller_find_sensor_data**
> InlineResponse200 sensors_controller_find_sensor_data(id, metrics, start_date, end_date)

Get data from a specified sensor

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sensors_api
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sensors_api.SensorsApi(api_client)
    id = "SPOT-0000" # str | 
    metrics = ["bottom_temperature","top_temperature"] # [str] | 
    start_date = "2021-01-10T12:00:00Z" # str | 
    end_date = "2021-05-10T12:00:00Z" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get data from a specified sensor
        api_response = api_instance.sensors_controller_find_sensor_data(id, metrics, start_date, end_date)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SensorsApi->sensors_controller_find_sensor_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **metrics** | **[str]**|  |
 **start_date** | **str**|  |
 **end_date** | **str**|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No data were found with the specified sensor id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_controller_find_sensor_surveys**
> sensors_controller_find_sensor_surveys(id)

Get surveys and survey media from a specified sensor

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sensors_api
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
    api_instance = sensors_api.SensorsApi(api_client)
    id = "SPOT-0000" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get surveys and survey media from a specified sensor
        api_instance.sensors_controller_find_sensor_surveys(id)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SensorsApi->sensors_controller_find_sensor_surveys: %s\n" % e)
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
**200** |  |  -  |
**404** | No surveys were found with the specified sensor id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_controller_find_sensors**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] sensors_controller_find_sensors()

Get all sites having sensors

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import sensors_api
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sensors_api.SensorsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all sites having sensors
        api_response = api_instance.sensors_controller_find_sensors()
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SensorsApi->sensors_controller_find_sensors: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

