# swagger_client.GoogleCloudStorageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**google_cloud_controller_delete_dangling_files**](GoogleCloudStorageApi.md#google_cloud_controller_delete_dangling_files) | **DELETE** /google-cloud/dangling | Deletes all unused files stored
[**google_cloud_controller_find_dangling_files**](GoogleCloudStorageApi.md#google_cloud_controller_find_dangling_files) | **GET** /google-cloud/dangling | Returns all files stored that are not used

# **google_cloud_controller_delete_dangling_files**
> google_cloud_controller_delete_dangling_files()

Deletes all unused files stored

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GoogleCloudStorageApi(swagger_client.ApiClient(configuration))

try:
    # Deletes all unused files stored
    api_instance.google_cloud_controller_delete_dangling_files()
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_controller_find_dangling_files**
> list[str] google_cloud_controller_find_dangling_files()

Returns all files stored that are not used

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GoogleCloudStorageApi(swagger_client.ApiClient(configuration))

try:
    # Returns all files stored that are not used
    api_response = api_instance.google_cloud_controller_find_dangling_files()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleCloudStorageApi->google_cloud_controller_find_dangling_files: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

