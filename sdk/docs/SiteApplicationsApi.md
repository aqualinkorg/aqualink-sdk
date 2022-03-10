# aqualink_sdk.SiteApplicationsApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**site_applications_controller_find_one_from_site**](SiteApplicationsApi.md#site_applications_controller_find_one_from_site) | **GET** /site-applications/sites/{siteId} | Returns site application of specified site
[**site_applications_controller_update**](SiteApplicationsApi.md#site_applications_controller_update) | **PUT** /site-applications/{appId}/sites/{siteId} | Updates site application by providing its appId. Needs authentication.


# **site_applications_controller_find_one_from_site**
> SiteApplication site_applications_controller_find_one_from_site(site_id)

Returns site application of specified site

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import site_applications_api
from aqualink_sdk.model.site_application import SiteApplication
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
    api_instance = site_applications_api.SiteApplicationsApi(api_client)
    site_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns site application of specified site
        api_response = api_instance.site_applications_controller_find_one_from_site(site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site application for specified site was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_applications_controller_update**
> SiteApplication site_applications_controller_update(app_id, inline_object)

Updates site application by providing its appId. Needs authentication.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import site_applications_api
from aqualink_sdk.model.inline_object import InlineObject
from aqualink_sdk.model.site_application import SiteApplication
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
    api_instance = site_applications_api.SiteApplicationsApi(api_client)
    app_id = 1 # float | 
    inline_object = InlineObject(
        site=UpdateSiteWithApplicationDto(
            name="Duxbury Site",
            depth=32,
        ),
        site_application=UpdateSiteApplicationDto(
            permit_requirements="Permit requirements",
            funding_source="Funding Source",
            installation_resources="Installation Resources",
            installation_schedule=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Updates site application by providing its appId. Needs authentication.
        api_response = api_instance.site_applications_controller_update(app_id, inline_object)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SiteApplicationsApi->site_applications_controller_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **float**|  |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**SiteApplication**](SiteApplication.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

