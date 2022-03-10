# aqualink_sdk.GoogleCloudStorageApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**google_cloud_controller_delete_dangling_files**](GoogleCloudStorageApi.md#google_cloud_controller_delete_dangling_files) | **DELETE** /google-cloud/dangling | Deletes all unused files stored
[**google_cloud_controller_find_dangling_files**](GoogleCloudStorageApi.md#google_cloud_controller_find_dangling_files) | **GET** /google-cloud/dangling | Returns all files stored that are not used


# **google_cloud_controller_delete_dangling_files**
> google_cloud_controller_delete_dangling_files()

Deletes all unused files stored

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import google_cloud_storage_api
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
    api_instance = google_cloud_storage_api.GoogleCloudStorageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Deletes all unused files stored
        api_instance.google_cloud_controller_delete_dangling_files()
    except aqualink_sdk.ApiException as e:
        print("Exception when calling GoogleCloudStorageApi->google_cloud_controller_delete_dangling_files: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_controller_find_dangling_files**
> [str] google_cloud_controller_find_dangling_files()

Returns all files stored that are not used

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import google_cloud_storage_api
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
    api_instance = google_cloud_storage_api.GoogleCloudStorageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all files stored that are not used
        api_response = api_instance.google_cloud_controller_find_dangling_files()
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling GoogleCloudStorageApi->google_cloud_controller_find_dangling_files: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of all dangling files |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

