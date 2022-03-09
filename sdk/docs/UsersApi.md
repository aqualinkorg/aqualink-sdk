# aqualink_sdk.UsersApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_controller_create**](UsersApi.md#users_controller_create) | **POST** /users | Creates a new user
[**users_controller_delete**](UsersApi.md#users_controller_delete) | **DELETE** /users/{id} | Deletes specified user
[**users_controller_get_administered_sites**](UsersApi.md#users_controller_get_administered_sites) | **GET** /users/current/administered-sites | Returns the administered sites of the signed in user
[**users_controller_get_self**](UsersApi.md#users_controller_get_self) | **GET** /users/current | Returns the currently signed in user
[**users_controller_set_admin_level**](UsersApi.md#users_controller_set_admin_level) | **PUT** /users/{id}/level | Updates the access level of a user

# **users_controller_create**
> User users_controller_create(body)

Creates a new user

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aqualink_sdk.UsersApi()
body = aqualink_sdk.CreateUserDto() # CreateUserDto | 

try:
    # Creates a new user
    api_response = api_instance.users_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserDto**](CreateUserDto.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_delete**
> users_controller_delete(id)

Deletes specified user

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.UsersApi(aqualink_sdk.ApiClient(configuration))
id = 1.2 # float | 

try:
    # Deletes specified user
    api_instance.users_controller_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_delete: %s\n" % e)
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

# **users_controller_get_administered_sites**
> list[Site] users_controller_get_administered_sites()

Returns the administered sites of the signed in user

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.UsersApi(aqualink_sdk.ApiClient(configuration))

try:
    # Returns the administered sites of the signed in user
    api_response = api_instance.users_controller_get_administered_sites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_get_administered_sites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Site]**](Site.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_self**
> User users_controller_get_self()

Returns the currently signed in user

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.UsersApi(aqualink_sdk.ApiClient(configuration))

try:
    # Returns the currently signed in user
    api_response = api_instance.users_controller_get_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_get_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_set_admin_level**
> users_controller_set_admin_level(body, id)

Updates the access level of a user

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.UsersApi(aqualink_sdk.ApiClient(configuration))
body = aqualink_sdk.SetAdminLevelDto() # SetAdminLevelDto | 
id = 1.2 # float | 

try:
    # Updates the access level of a user
    api_instance.users_controller_set_admin_level(body, id)
except ApiException as e:
    print("Exception when calling UsersApi->users_controller_set_admin_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetAdminLevelDto**](SetAdminLevelDto.md)|  | 
 **id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

