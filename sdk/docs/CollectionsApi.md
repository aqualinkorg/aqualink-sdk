# aqualink_sdk.CollectionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_controller_create**](CollectionsApi.md#collections_controller_create) | **POST** /collections | Creates a new collection
[**collections_controller_delete**](CollectionsApi.md#collections_controller_delete) | **DELETE** /collections/{collectionId} | Delete specified collection
[**collections_controller_find**](CollectionsApi.md#collections_controller_find) | **GET** /collections | Fetch all user&#x27;s private collections
[**collections_controller_find_one**](CollectionsApi.md#collections_controller_find_one) | **GET** /collections/{collectionId} | Fetch detailed data from specified private collection
[**collections_controller_find_one_public**](CollectionsApi.md#collections_controller_find_one_public) | **GET** /collections/public/{collectionId} | Fetch detailed data from specified public collection
[**collections_controller_find_public**](CollectionsApi.md#collections_controller_find_public) | **GET** /collections/public | Fetch all public collections
[**collections_controller_get_heat_stress_tracker**](CollectionsApi.md#collections_controller_get_heat_stress_tracker) | **GET** /collections/heat-stress-tracker | Fetch the heat stress tracker
[**collections_controller_update**](CollectionsApi.md#collections_controller_update) | **PUT** /collections/{collectionId} | Update specified collection

# **collections_controller_create**
> Collection collections_controller_create(body)

Creates a new collection

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.CollectionsApi(aqualink_sdk.ApiClient(configuration))
body = aqualink_sdk.CreateCollectionDto() # CreateCollectionDto | 

try:
    # Creates a new collection
    api_response = api_instance.collections_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCollectionDto**](CreateCollectionDto.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_delete**
> collections_controller_delete(collection_id)

Delete specified collection

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.CollectionsApi(aqualink_sdk.ApiClient(configuration))
collection_id = 1.2 # float | 

try:
    # Delete specified collection
    api_instance.collections_controller_delete(collection_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_find**
> list[Collection] collections_controller_find(name=name, site_id=site_id)

Fetch all user's private collections

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.CollectionsApi(aqualink_sdk.ApiClient(configuration))
name = 'name_example' # str |  (optional)
site_id = 1.2 # float |  (optional)

try:
    # Fetch all user's private collections
    api_response = api_instance.collections_controller_find(name=name, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_controller_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **site_id** | **float**|  | [optional] 

### Return type

[**list[Collection]**](Collection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_find_one**
> Collection collections_controller_find_one(collection_id)

Fetch detailed data from specified private collection

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.CollectionsApi(aqualink_sdk.ApiClient(configuration))
collection_id = 1.2 # float | 

try:
    # Fetch detailed data from specified private collection
    api_response = api_instance.collections_controller_find_one(collection_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_find_one_public**
> Collection collections_controller_find_one_public(collection_id)

Fetch detailed data from specified public collection

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aqualink_sdk.CollectionsApi()
collection_id = 1.2 # float | 

try:
    # Fetch detailed data from specified public collection
    api_response = api_instance.collections_controller_find_one_public(collection_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_find_public**
> list[Collection] collections_controller_find_public(name=name, site_id=site_id)

Fetch all public collections

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aqualink_sdk.CollectionsApi()
name = 'name_example' # str |  (optional)
site_id = 1.2 # float |  (optional)

try:
    # Fetch all public collections
    api_response = api_instance.collections_controller_find_public(name=name, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_controller_find_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **site_id** | **float**|  | [optional] 

### Return type

[**list[Collection]**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_get_heat_stress_tracker**
> object collections_controller_get_heat_stress_tracker()

Fetch the heat stress tracker

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aqualink_sdk.CollectionsApi()

try:
    # Fetch the heat stress tracker
    api_response = api_instance.collections_controller_get_heat_stress_tracker()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_controller_get_heat_stress_tracker: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_controller_update**
> Collection collections_controller_update(body, collection_id)

Update specified collection

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.CollectionsApi(aqualink_sdk.ApiClient(configuration))
body = aqualink_sdk.UpdateCollectionDto() # UpdateCollectionDto | 
collection_id = 1.2 # float | 

try:
    # Update specified collection
    api_response = api_instance.collections_controller_update(body, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCollectionDto**](UpdateCollectionDto.md)|  | 
 **collection_id** | **float**|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

