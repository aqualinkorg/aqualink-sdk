# aqualink_sdk.SurveysApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**surveys_controller_create**](SurveysApi.md#surveys_controller_create) | **POST** /sites/{siteId}/surveys | Creates a new survey
[**surveys_controller_create_media**](SurveysApi.md#surveys_controller_create_media) | **POST** /sites/{siteId}/surveys/{id}/media | Creates a new survey media
[**surveys_controller_delete**](SurveysApi.md#surveys_controller_delete) | **DELETE** /sites/{siteId}/surveys/{id} | Deletes a specified survey
[**surveys_controller_delete_media**](SurveysApi.md#surveys_controller_delete_media) | **DELETE** /sites/{siteId}/surveys/media/{id} | Deletes a specified survey media
[**surveys_controller_find**](SurveysApi.md#surveys_controller_find) | **GET** /sites/{siteId}/surveys | Returns all site&#39;s survey
[**surveys_controller_find_media**](SurveysApi.md#surveys_controller_find_media) | **GET** /sites/{siteId}/surveys/{id}/media | Returns all media of a specified survey
[**surveys_controller_find_one**](SurveysApi.md#surveys_controller_find_one) | **GET** /sites/{siteId}/surveys/{id} | Returns specified survey
[**surveys_controller_update**](SurveysApi.md#surveys_controller_update) | **PUT** /sites/{siteId}/surveys/{id} | Updates a specified survey
[**surveys_controller_update_media**](SurveysApi.md#surveys_controller_update_media) | **PUT** /sites/{siteId}/surveys/media/{id} | Updates a specified survey media
[**surveys_controller_upload**](SurveysApi.md#surveys_controller_upload) | **POST** /sites/{siteId}/surveys/upload | Uploads a new survey media


# **surveys_controller_create**
> Survey surveys_controller_create(site_id, create_survey_dto)

Creates a new survey

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
from aqualink_sdk.model.survey import Survey
from aqualink_sdk.model.create_survey_dto import CreateSurveyDto
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
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    create_survey_dto = CreateSurveyDto(
        comments="Survey comments",
        dive_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        weather_conditions="calm",
    ) # CreateSurveyDto | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new survey
        api_response = api_instance.surveys_controller_create(site_id, create_survey_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **create_survey_dto** | [**CreateSurveyDto**](CreateSurveyDto.md)|  |

### Return type

[**Survey**](Survey.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**404** | No site was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_create_media**
> SurveyMedia surveys_controller_create_media(site_id, id, create_survey_media_dto)

Creates a new survey media

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
from aqualink_sdk.model.create_survey_media_dto import CreateSurveyMediaDto
from aqualink_sdk.model.survey_media import SurveyMedia
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
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    id = 1 # float | 
    create_survey_media_dto = CreateSurveyMediaDto(
        url="https://storage.googleapis.com/storage/reef-image-564894612222.jpg",
        comments="Survey Media comments",
        quality=1,
        featured=False,
        hidden=False,
        metadata={},
        observations="anthropogenic",
        survey_point_id=3.14,
    ) # CreateSurveyMediaDto | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new survey media
        api_response = api_instance.surveys_controller_create_media(site_id, id, create_survey_media_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_create_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **id** | **float**|  |
 **create_survey_media_dto** | [**CreateSurveyMediaDto**](CreateSurveyMediaDto.md)|  |

### Return type

[**SurveyMedia**](SurveyMedia.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**404** | No survey was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_delete**
> surveys_controller_delete(site_id, id)

Deletes a specified survey

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
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
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specified survey
        api_instance.surveys_controller_delete(site_id, id)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
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
**404** | No survey was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_delete_media**
> surveys_controller_delete_media(site_id, id)

Deletes a specified survey media

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
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
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specified survey media
        api_instance.surveys_controller_delete_media(site_id, id)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_delete_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
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
**404** | No survey media was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_find**
> [Survey] surveys_controller_find(site_id)

Returns all site's survey

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
from aqualink_sdk.model.survey import Survey
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns all site's survey
        api_response = api_instance.surveys_controller_find(site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |

### Return type

[**[Survey]**](Survey.md)

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

# **surveys_controller_find_media**
> [SurveyMedia] surveys_controller_find_media(site_id, id)

Returns all media of a specified survey

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
from aqualink_sdk.model.survey_media import SurveyMedia
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns all media of a specified survey
        api_response = api_instance.surveys_controller_find_media(site_id, id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_find_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **id** | **float**|  |

### Return type

[**[SurveyMedia]**](SurveyMedia.md)

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

# **surveys_controller_find_one**
> Survey surveys_controller_find_one(site_id, id)

Returns specified survey

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
from aqualink_sdk.model.survey import Survey
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
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns specified survey
        api_response = api_instance.surveys_controller_find_one(site_id, id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_find_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **id** | **float**|  |

### Return type

[**Survey**](Survey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No survey was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_update**
> Survey surveys_controller_update(site_id, id, edit_survey_dto)

Updates a specified survey

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
from aqualink_sdk.model.survey import Survey
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.edit_survey_dto import EditSurveyDto
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
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    id = 1 # float | 
    edit_survey_dto = EditSurveyDto(
        comments="Survey comments",
        dive_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        weather_conditions="calm",
    ) # EditSurveyDto | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a specified survey
        api_response = api_instance.surveys_controller_update(site_id, id, edit_survey_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **id** | **float**|  |
 **edit_survey_dto** | [**EditSurveyDto**](EditSurveyDto.md)|  |

### Return type

[**Survey**](Survey.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No survey was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_update_media**
> SurveyMedia surveys_controller_update_media(site_id, id, edit_survey_media_dto)

Updates a specified survey media

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
from aqualink_sdk.model.edit_survey_media_dto import EditSurveyMediaDto
from aqualink_sdk.model.survey_media import SurveyMedia
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
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    id = 1 # float | 
    edit_survey_media_dto = EditSurveyMediaDto(
        comments="Survey media comments",
        survey_point_id=1,
        featured=False,
        hidden=False,
        observations="anthropogenic",
    ) # EditSurveyMediaDto | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a specified survey media
        api_response = api_instance.surveys_controller_update_media(site_id, id, edit_survey_media_dto)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_update_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **id** | **float**|  |
 **edit_survey_media_dto** | [**EditSurveyMediaDto**](EditSurveyMediaDto.md)|  |

### Return type

[**SurveyMedia**](SurveyMedia.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No survey media was found with the specified id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_upload**
> str surveys_controller_upload(site_id)

Uploads a new survey media

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import aqualink_sdk
from aqualink_sdk.api import surveys_api
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
    api_instance = surveys_api.SurveysApi(api_client)
    site_id = 1 # float | 
    file = open('/path/to/file', 'rb') # file_type | The image to upload (image/jpeg, image/png, image/tiff). Max size: 50MB (optional)

    # example passing only required values which don't have defaults set
    try:
        # Uploads a new survey media
        api_response = api_instance.surveys_controller_upload(site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_upload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Uploads a new survey media
        api_response = api_instance.surveys_controller_upload(site_id, file=file)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling SurveysApi->surveys_controller_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **file** | **file_type**| The image to upload (image/jpeg, image/png, image/tiff). Max size: 50MB | [optional]

### Return type

**str**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the public url to access the uploaded media |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

