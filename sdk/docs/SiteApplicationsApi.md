# swagger_client.SiteApplicationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**site_applications_controller_find_one_from_site**](SiteApplicationsApi.md#site_applications_controller_find_one_from_site) | **GET** /site-applications/sites/{siteId} | Returns site application of specified site
[**site_applications_controller_update**](SiteApplicationsApi.md#site_applications_controller_update) | **PUT** /site-applications/{appId}/sites/{siteId} | Updates site application by providing its appId. Needs authentication.

# **site_applications_controller_find_one_from_site**
> SiteApplication site_applications_controller_find_one_from_site(site_id)

Returns site application of specified site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SiteApplicationsApi(swagger_client.ApiClient(configuration))
site_id = 1.2 # float | 

try:
    # Returns site application of specified site
    api_response = api_instance.site_applications_controller_find_one_from_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApplicationsApi->site_applications_controller_find_one_from_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  | 

### Return type

[**SiteApplication**](SiteApplication.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_applications_controller_update**
> SiteApplication site_applications_controller_update(body, app_id)

Updates site application by providing its appId. Needs authentication.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SiteApplicationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SitesSiteIdBody() # SitesSiteIdBody | 
app_id = 1.2 # float | 

try:
    # Updates site application by providing its appId. Needs authentication.
    api_response = api_instance.site_applications_controller_update(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApplicationsApi->site_applications_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SitesSiteIdBody**](SitesSiteIdBody.md)|  | 
 **app_id** | **float**|  | 

### Return type

[**SiteApplication**](SiteApplication.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

