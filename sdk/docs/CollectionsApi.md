# aqualink_sdk.CollectionsApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_controller_create**](CollectionsApi.md#collections_controller_create) | **POST** /collections | Creates a new collection
[**collections_controller_delete**](CollectionsApi.md#collections_controller_delete) | **DELETE** /collections/{collectionId} | Delete specified collection
[**collections_controller_find**](CollectionsApi.md#collections_controller_find) | **GET** /collections | Fetch all user&#39;s private collections
[**collections_controller_find_one**](CollectionsApi.md#collections_controller_find_one) | **GET** /collections/{collectionId} | Fetch detailed data from specified private collection
[**collections_controller_find_one_public**](CollectionsApi.md#collections_controller_find_one_public) | **GET** /collections/public/{collectionId} | Fetch detailed data from specified public collection
[**collections_controller_find_public**](CollectionsApi.md#collections_controller_find_public) | **GET** /collections/public | Fetch all public collections
[**collections_controller_get_heat_stress_tracker**](CollectionsApi.md#collections_controller_get_heat_stress_tracker) | **GET** /collections/heat-stress-tracker | Fetch the heat stress tracker
[**collections_controller_update**](CollectionsApi.md#collections_controller_update) | **PUT** /collections/{collectionId} | Update specified collection


# **collections_controller_create**
> Collection collections_controller_create(create_collection_dto)

Creates a new collection

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import collections_api
from aqualink_sdk.model.collection import Collection
from aqualink_sdk.model.create_collection_dto import CreateCollectionDto
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
    api_instance = collections_api.CollectionsApi(api_client)
    create_collection_dto = CreateCollectionDto(
        name="La Niña heatwave 20/21",
        user_id=1,
        site_ids=[1,3,5],
        is_public=True,
    ) # CreateCollectionDto | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new collection
        api_response = api_instance.collections_controller_create(create_collection_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling CollectionsApi->collections_controller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_collection_dto** | [**CreateCollectionDto**](CreateCollectionDto.md)|  |

### Return type

[**Collection**](Collection.md)

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

# **collections_controller_delete**
> collections_controller_delete(collection_id)

Delete specified collection

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import collections_api
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Delete specified collection
        api_instance.collections_controller_delete(collection_id)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling CollectionsApi->collections_controller_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **float**|  |

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
**404** | No collection was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_find**
> [Collection] collections_controller_find()

Fetch all user's private collections

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import collections_api
from aqualink_sdk.model.collection import Collection
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
    api_instance = collections_api.CollectionsApi(api_client)
    name = "La Niña heatwave 20/21" # str |  (optional)
    site_id = 1 # float |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all user's private collections
        api_response = api_instance.collections_controller_find(name=name, site_id=site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling CollectionsApi->collections_controller_find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]
 **site_id** | **float**|  | [optional]

### Return type

[**[Collection]**](Collection.md)

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

# **collections_controller_find_one**
> Collection collections_controller_find_one(collection_id)

Fetch detailed data from specified private collection

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import collections_api
from aqualink_sdk.model.inline_response401 import InlineResponse401
from aqualink_sdk.model.collection import Collection
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch detailed data from specified private collection
        api_response = api_instance.collections_controller_find_one(collection_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling CollectionsApi->collections_controller_find_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **float**|  |

### Return type

[**Collection**](Collection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Collection selected is not public |  -  |
**404** | No collection was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_find_one_public**
> Collection collections_controller_find_one_public(collection_id)

Fetch detailed data from specified public collection

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import collections_api
from aqualink_sdk.model.collection import Collection
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch detailed data from specified public collection
        api_response = api_instance.collections_controller_find_one_public(collection_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling CollectionsApi->collections_controller_find_one_public: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **float**|  |

### Return type

[**Collection**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No collection was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_find_public**
> [Collection] collections_controller_find_public()

Fetch all public collections

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import collections_api
from aqualink_sdk.model.collection import Collection
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = collections_api.CollectionsApi(api_client)
    name = "La Niña heatwave 20/21" # str |  (optional)
    site_id = 1 # float |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all public collections
        api_response = api_instance.collections_controller_find_public(name=name, site_id=site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling CollectionsApi->collections_controller_find_public: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]
 **site_id** | **float**|  | [optional]

### Return type

[**[Collection]**](Collection.md)

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

# **collections_controller_get_heat_stress_tracker**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} collections_controller_get_heat_stress_tracker()

Fetch the heat stress tracker

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import collections_api
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = collections_api.CollectionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the heat stress tracker
        api_response = api_instance.collections_controller_get_heat_stress_tracker()
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling CollectionsApi->collections_controller_get_heat_stress_tracker: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **collections_controller_update**
> Collection collections_controller_update(collection_id, update_collection_dto)

Update specified collection

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import collections_api
from aqualink_sdk.model.collection import Collection
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.update_collection_dto import UpdateCollectionDto
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = 1 # float | 
    update_collection_dto = UpdateCollectionDto(
        name="La Niña heatwave 20/21",
        user_id=1,
        add_site_ids=[1,3,4],
        remove_site_ids=[1,4,5],
        is_public=True,
    ) # UpdateCollectionDto | 

    # example passing only required values which don't have defaults set
    try:
        # Update specified collection
        api_response = api_instance.collections_controller_update(collection_id, update_collection_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling CollectionsApi->collections_controller_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **float**|  |
 **update_collection_dto** | [**UpdateCollectionDto**](UpdateCollectionDto.md)|  |

### Return type

[**Collection**](Collection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No collection was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

