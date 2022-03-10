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
> User users_controller_create(create_user_dto)

Creates a new user

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import users_api
from aqualink_sdk.model.user import User
from aqualink_sdk.model.create_user_dto import CreateUserDto
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    create_user_dto = CreateUserDto(
        full_name="User full name",
        email="fullname@example.com",
        organization="Ovio",
        location=RegionPolygon(
            type="Point",
            coordinates=[15.24012,-10.05412],
        ),
        country="United States",
        description="Some description",
        image_url="http://some-sample-url.com",
    ) # CreateUserDto | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new user
        api_response = api_instance.users_controller_create(create_user_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling UsersApi->users_controller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_dto** | [**CreateUserDto**](CreateUserDto.md)|  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_delete**
> users_controller_delete(id)

Deletes specified user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes specified user
        api_instance.users_controller_delete(id)
    except aqualink_sdk.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No user was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_administered_sites**
> [Site] users_controller_get_administered_sites()

Returns the administered sites of the signed in user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import users_api
from aqualink_sdk.model.site import Site
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the administered sites of the signed in user
        api_response = api_instance.users_controller_get_administered_sites()
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling UsersApi->users_controller_get_administered_sites: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Site]**](Site.md)

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

# **users_controller_get_self**
> User users_controller_get_self()

Returns the currently signed in user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import users_api
from aqualink_sdk.model.user import User
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the currently signed in user
        api_response = api_instance.users_controller_get_self()
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_set_admin_level**
> users_controller_set_admin_level(id, set_admin_level_dto)

Updates the access level of a user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import users_api
from aqualink_sdk.model.set_admin_level_dto import SetAdminLevelDto
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
    api_instance = users_api.UsersApi(api_client)
    id = 1 # float | 
    set_admin_level_dto = SetAdminLevelDto(
        level="default",
    ) # SetAdminLevelDto | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the access level of a user
        api_instance.users_controller_set_admin_level(id, set_admin_level_dto)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling UsersApi->users_controller_set_admin_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **set_admin_level_dto** | [**SetAdminLevelDto**](SetAdminLevelDto.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No user was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

