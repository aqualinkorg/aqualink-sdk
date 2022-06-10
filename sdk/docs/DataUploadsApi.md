# aqualink_sdk.DataUploadsApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_uploads_controller_delete_data_uploads**](DataUploadsApi.md#data_uploads_controller_delete_data_uploads) | **POST** /data-uploads/delete-uploads | Delete selected data uploads
[**data_uploads_controller_get_data_uploads**](DataUploadsApi.md#data_uploads_controller_get_data_uploads) | **GET** /data-uploads/sites/{siteId} | Find all data uploads for a site&#39;s survey point


# **data_uploads_controller_delete_data_uploads**
> data_uploads_controller_delete_data_uploads(data_uploads_delete_dto)

Delete selected data uploads

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import data_uploads_api
from aqualink_sdk.model.data_uploads_delete_dto import DataUploadsDeleteDto
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_uploads_api.DataUploadsApi(api_client)
    data_uploads_delete_dto = DataUploadsDeleteDto(
        ids=[1,2],
    ) # DataUploadsDeleteDto | 

    # example passing only required values which don't have defaults set
    try:
        # Delete selected data uploads
        api_instance.data_uploads_controller_delete_data_uploads(data_uploads_delete_dto)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling DataUploadsApi->data_uploads_controller_delete_data_uploads: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_uploads_delete_dto** | [**DataUploadsDeleteDto**](DataUploadsDeleteDto.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_uploads_controller_get_data_uploads**
> [DataUploads] data_uploads_controller_get_data_uploads(site_id)

Find all data uploads for a site's survey point

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import data_uploads_api
from aqualink_sdk.model.data_uploads import DataUploads
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_uploads_api.DataUploadsApi(api_client)
    site_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Find all data uploads for a site's survey point
        api_response = api_instance.data_uploads_controller_get_data_uploads(site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling DataUploadsApi->data_uploads_controller_get_data_uploads: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |

### Return type

[**[DataUploads]**](DataUploads.md)

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

