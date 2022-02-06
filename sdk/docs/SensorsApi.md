# swagger_client.SensorsApi

All URIs are relative to */*

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
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()
id = 'id_example' # str | 
metrics = ['metrics_example'] # list[str] | 
start_date = 'start_date_example' # str | 
end_date = 'end_date_example' # str | 

try:
    # Get data from a specified sensor
    api_response = api_instance.sensors_controller_find_sensor_data(id, metrics, start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_controller_find_sensor_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **metrics** | [**list[str]**](str.md)|  | 
 **start_date** | **str**|  | 
 **end_date** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_controller_find_sensor_surveys**
> sensors_controller_find_sensor_surveys(id)

Get surveys and survey media from a specified sensor

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()
id = 'id_example' # str | 

try:
    # Get surveys and survey media from a specified sensor
    api_instance.sensors_controller_find_sensor_surveys(id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_controller_find_sensors**
> list[object] sensors_controller_find_sensors()

Get all sites having sensors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorsApi()

try:
    # Get all sites having sensors
    api_response = api_instance.sensors_controller_find_sensors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_controller_find_sensors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

