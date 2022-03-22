# aqualink_sdk.SitePointsOfInterestApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**site_survey_points_controller_create**](SitePointsOfInterestApi.md#site_survey_points_controller_create) | **POST** /site-survey-points | Creates a new site point of interest
[**site_survey_points_controller_delete**](SitePointsOfInterestApi.md#site_survey_points_controller_delete) | **DELETE** /site-survey-points/{id} | Deletes specified site point of interest
[**site_survey_points_controller_find**](SitePointsOfInterestApi.md#site_survey_points_controller_find) | **GET** /site-survey-points | Returns site points of interest filtered by the provided filters
[**site_survey_points_controller_find_one**](SitePointsOfInterestApi.md#site_survey_points_controller_find_one) | **GET** /site-survey-points/{id} | Returns specified site point of interest
[**site_survey_points_controller_update**](SitePointsOfInterestApi.md#site_survey_points_controller_update) | **PUT** /site-survey-points/{id} | Updates specified site point of interest


# **site_survey_points_controller_create**
> SiteSurveyPoint site_survey_points_controller_create(create_site_survey_point_dto)

Creates a new site point of interest

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import site_points_of_interest_api
from aqualink_sdk.model.site_survey_point import SiteSurveyPoint
from aqualink_sdk.model.create_site_survey_point_dto import CreateSiteSurveyPointDto
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
    api_instance = site_points_of_interest_api.SitePointsOfInterestApi(api_client)
    create_site_survey_point_dto = CreateSiteSurveyPointDto(
        name="Outer tide pool",
        latitude=12.4344,
        longitude=-21.2233,
        survey_point_label_id=1,
        image_url="http://some-sample-url.com",
        site_id=2,
    ) # CreateSiteSurveyPointDto | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new site point of interest
        api_response = api_instance.site_survey_points_controller_create(create_site_survey_point_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitePointsOfInterestApi->site_survey_points_controller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_site_survey_point_dto** | [**CreateSiteSurveyPointDto**](CreateSiteSurveyPointDto.md)|  |

### Return type

[**SiteSurveyPoint**](SiteSurveyPoint.md)

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

# **site_survey_points_controller_delete**
> site_survey_points_controller_delete(id)

Deletes specified site point of interest

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import site_points_of_interest_api
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
    api_instance = site_points_of_interest_api.SitePointsOfInterestApi(api_client)
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes specified site point of interest
        api_instance.site_survey_points_controller_delete(id)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitePointsOfInterestApi->site_survey_points_controller_delete: %s\n" % e)
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
**404** | No site point of interest was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_survey_points_controller_find**
> [SiteSurveyPoint] site_survey_points_controller_find()

Returns site points of interest filtered by the provided filters

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import site_points_of_interest_api
from aqualink_sdk.model.site_survey_point import SiteSurveyPoint
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = site_points_of_interest_api.SitePointsOfInterestApi(api_client)
    name = "Outer tide pool" # str |  (optional)
    site_id = 1 # float |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns site points of interest filtered by the provided filters
        api_response = api_instance.site_survey_points_controller_find(name=name, site_id=site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitePointsOfInterestApi->site_survey_points_controller_find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]
 **site_id** | **float**|  | [optional]

### Return type

[**[SiteSurveyPoint]**](SiteSurveyPoint.md)

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

# **site_survey_points_controller_find_one**
> SiteSurveyPoint site_survey_points_controller_find_one(id)

Returns specified site point of interest

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import site_points_of_interest_api
from aqualink_sdk.model.site_survey_point import SiteSurveyPoint
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
    api_instance = site_points_of_interest_api.SitePointsOfInterestApi(api_client)
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns specified site point of interest
        api_response = api_instance.site_survey_points_controller_find_one(id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitePointsOfInterestApi->site_survey_points_controller_find_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |

### Return type

[**SiteSurveyPoint**](SiteSurveyPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site point of interest was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_survey_points_controller_update**
> SiteSurveyPoint site_survey_points_controller_update(id, update_site_survey_point_dto)

Updates specified site point of interest

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import site_points_of_interest_api
from aqualink_sdk.model.site_survey_point import SiteSurveyPoint
from aqualink_sdk.model.update_site_survey_point_dto import UpdateSiteSurveyPointDto
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
    api_instance = site_points_of_interest_api.SitePointsOfInterestApi(api_client)
    id = 1 # float | 
    update_site_survey_point_dto = UpdateSiteSurveyPointDto(
        name="Outer tide pool",
        latitude=1.21123,
        longitude=94.22121,
        survey_point_label_id=1,
        image_url="http://some-sample-url.com",
        site_id=1,
    ) # UpdateSiteSurveyPointDto | 

    # example passing only required values which don't have defaults set
    try:
        # Updates specified site point of interest
        api_response = api_instance.site_survey_points_controller_update(id, update_site_survey_point_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SitePointsOfInterestApi->site_survey_points_controller_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **update_site_survey_point_dto** | [**UpdateSiteSurveyPointDto**](UpdateSiteSurveyPointDto.md)|  |

### Return type

[**SiteSurveyPoint**](SiteSurveyPoint.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No site point of interest was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

