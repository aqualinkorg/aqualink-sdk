# swagger_client.DataUploadsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_uploads_controller_get_data_uploads**](DataUploadsApi.md#data_uploads_controller_get_data_uploads) | **GET** /data-uploads/sites/{siteId} | Find all data uploads for a site&#x27;s survey point

# **data_uploads_controller_get_data_uploads**
> list[DataUploads] data_uploads_controller_get_data_uploads(site_id)

Find all data uploads for a site's survey point

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataUploadsApi()
site_id = 1.2 # float | 

try:
    # Find all data uploads for a site's survey point
    api_response = api_instance.data_uploads_controller_get_data_uploads(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataUploadsApi->data_uploads_controller_get_data_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  | 

### Return type

[**list[DataUploads]**](DataUploads.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

