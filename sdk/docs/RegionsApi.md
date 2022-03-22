# aqualink_sdk.RegionsApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regions_controller_create**](RegionsApi.md#regions_controller_create) | **POST** /regions | Creates new region
[**regions_controller_delete**](RegionsApi.md#regions_controller_delete) | **DELETE** /regions/{id} | Deletes specified region
[**regions_controller_find**](RegionsApi.md#regions_controller_find) | **GET** /regions | Returns regions filtered by provided filters
[**regions_controller_find_one**](RegionsApi.md#regions_controller_find_one) | **GET** /regions/{id} | Returns specified region
[**regions_controller_update**](RegionsApi.md#regions_controller_update) | **PUT** /regions/{id} | Updates specified region


# **regions_controller_create**
> Region regions_controller_create(create_region_dto)

Creates new region

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import regions_api
from aqualink_sdk.model.create_region_dto import CreateRegionDto
from aqualink_sdk.model.region import Region
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
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
    api_instance = regions_api.RegionsApi(api_client)
    create_region_dto = CreateRegionDto(
        name="United States",
        polygon=CreateRegionDtoPolygon(
            type="Point",
            coordinates=[15.24012,-10.05412],
        ),
        parent_id=1,
    ) # CreateRegionDto | 

    # example passing only required values which don't have defaults set
    try:
        # Creates new region
        api_response = api_instance.regions_controller_create(create_region_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling RegionsApi->regions_controller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_region_dto** | [**CreateRegionDto**](CreateRegionDto.md)|  |

### Return type

[**Region**](Region.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_controller_delete**
> regions_controller_delete(id)

Deletes specified region

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import regions_api
from aqualink_sdk.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
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
    api_instance = regions_api.RegionsApi(api_client)
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes specified region
        api_instance.regions_controller_delete(id)
    except aqualink_sdk.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No region was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_controller_find**
> [Region] regions_controller_find()

Returns regions filtered by provided filters

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import regions_api
from aqualink_sdk.model.region import Region
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = regions_api.RegionsApi(api_client)
    name = "United States" # str |  (optional)
    parent = 1 # float |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns regions filtered by provided filters
        api_response = api_instance.regions_controller_find(name=name, parent=parent)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling RegionsApi->regions_controller_find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]
 **parent** | **float**|  | [optional]

### Return type

[**[Region]**](Region.md)

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

# **regions_controller_find_one**
> Region regions_controller_find_one(id)

Returns specified region

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import regions_api
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.region import Region
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = regions_api.RegionsApi(api_client)
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns specified region
        api_response = api_instance.regions_controller_find_one(id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No region was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_controller_update**
> Region regions_controller_update(id, update_region_dto)

Updates specified region

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import regions_api
from aqualink_sdk.model.update_region_dto import UpdateRegionDto
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.region import Region
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
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
    api_instance = regions_api.RegionsApi(api_client)
    id = 1 # float | 
    update_region_dto = UpdateRegionDto(
        name="United States",
        polygon=CreateRegionDtoPolygon(
            type="Point",
            coordinates=[15.24012,-10.05412],
        ),
        parent_id=1,
    ) # UpdateRegionDto | 

    # example passing only required values which don't have defaults set
    try:
        # Updates specified region
        api_response = api_instance.regions_controller_update(id, update_region_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling RegionsApi->regions_controller_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **update_region_dto** | [**UpdateRegionDto**](UpdateRegionDto.md)|  |

### Return type

[**Region**](Region.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No region was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

