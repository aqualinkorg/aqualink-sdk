# swagger_client.RegionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regions_controller_create**](RegionsApi.md#regions_controller_create) | **POST** /regions | Creates new region
[**regions_controller_delete**](RegionsApi.md#regions_controller_delete) | **DELETE** /regions/{id} | Deletes specified region
[**regions_controller_find**](RegionsApi.md#regions_controller_find) | **GET** /regions | Returns regions filtered by provided filters
[**regions_controller_find_one**](RegionsApi.md#regions_controller_find_one) | **GET** /regions/{id} | Returns specified region
[**regions_controller_update**](RegionsApi.md#regions_controller_update) | **PUT** /regions/{id} | Updates specified region

# **regions_controller_create**
> Region regions_controller_create(body)

Creates new region

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRegionDto() # CreateRegionDto | 

try:
    # Creates new region
    api_response = api_instance.regions_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->regions_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRegionDto**](CreateRegionDto.md)|  | 

### Return type

[**Region**](Region.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_controller_delete**
> regions_controller_delete(id)

Deletes specified region

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
id = 1.2 # float | 

try:
    # Deletes specified region
    api_instance.regions_controller_delete(id)
except ApiException as e:
    print("Exception when calling RegionsApi->regions_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_controller_find**
> list[Region] regions_controller_find(name=name, parent=parent)

Returns regions filtered by provided filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RegionsApi()
name = 'name_example' # str |  (optional)
parent = 1.2 # float |  (optional)

try:
    # Returns regions filtered by provided filters
    api_response = api_instance.regions_controller_find(name=name, parent=parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->regions_controller_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **parent** | **float**|  | [optional] 

### Return type

[**list[Region]**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_controller_find_one**
> Region regions_controller_find_one(id)

Returns specified region

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RegionsApi()
id = 1.2 # float | 

try:
    # Returns specified region
    api_response = api_instance.regions_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->regions_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_controller_update**
> Region regions_controller_update(body, id)

Updates specified region

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateRegionDto() # UpdateRegionDto | 
id = 1.2 # float | 

try:
    # Updates specified region
    api_response = api_instance.regions_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->regions_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRegionDto**](UpdateRegionDto.md)|  | 
 **id** | **float**|  | 

### Return type

[**Region**](Region.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

