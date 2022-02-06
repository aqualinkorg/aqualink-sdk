# aqualink_sdk.SurveysApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**surveys_controller_create**](SurveysApi.md#surveys_controller_create) | **POST** /sites/{siteId}/surveys | Creates a new survey
[**surveys_controller_create_media**](SurveysApi.md#surveys_controller_create_media) | **POST** /sites/{siteId}/surveys/{id}/media | Creates a new survey media
[**surveys_controller_delete**](SurveysApi.md#surveys_controller_delete) | **DELETE** /sites/{siteId}/surveys/{id} | Deletes a specified survey
[**surveys_controller_delete_media**](SurveysApi.md#surveys_controller_delete_media) | **DELETE** /sites/{siteId}/surveys/media/{id} | Deletes a specified survey media
[**surveys_controller_find**](SurveysApi.md#surveys_controller_find) | **GET** /sites/{siteId}/surveys | Returns all site&#x27;s survey
[**surveys_controller_find_media**](SurveysApi.md#surveys_controller_find_media) | **GET** /sites/{siteId}/surveys/{id}/media | Returns all media of a specified survey
[**surveys_controller_find_one**](SurveysApi.md#surveys_controller_find_one) | **GET** /sites/{siteId}/surveys/{id} | Returns specified survey
[**surveys_controller_update**](SurveysApi.md#surveys_controller_update) | **PUT** /sites/{siteId}/surveys/{id} | Updates a specified survey
[**surveys_controller_update_media**](SurveysApi.md#surveys_controller_update_media) | **PUT** /sites/{siteId}/surveys/media/{id} | Updates a specified survey media
[**surveys_controller_upload**](SurveysApi.md#surveys_controller_upload) | **POST** /sites/{siteId}/surveys/upload | Uploads a new survey media

# **surveys_controller_create**
> Survey surveys_controller_create(body, site_id)

Creates a new survey

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi(aqualink_sdk.ApiClient(configuration))
body = aqualink_sdk.CreateSurveyDto() # CreateSurveyDto | 
site_id = 1.2 # float | 

try:
    # Creates a new survey
    api_response = api_instance.surveys_controller_create(body, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->surveys_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSurveyDto**](CreateSurveyDto.md)|  | 
 **site_id** | **float**|  | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_create_media**
> SurveyMedia surveys_controller_create_media(body, site_id, id)

Creates a new survey media

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi(aqualink_sdk.ApiClient(configuration))
body = aqualink_sdk.CreateSurveyMediaDto() # CreateSurveyMediaDto | 
site_id = 1.2 # float | 
id = 1.2 # float | 

try:
    # Creates a new survey media
    api_response = api_instance.surveys_controller_create_media(body, site_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->surveys_controller_create_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSurveyMediaDto**](CreateSurveyMediaDto.md)|  | 
 **site_id** | **float**|  | 
 **id** | **float**|  | 

### Return type

[**SurveyMedia**](SurveyMedia.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_delete**
> surveys_controller_delete(site_id, id)

Deletes a specified survey

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi(aqualink_sdk.ApiClient(configuration))
site_id = 1.2 # float | 
id = 1.2 # float | 

try:
    # Deletes a specified survey
    api_instance.surveys_controller_delete(site_id, id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_delete_media**
> surveys_controller_delete_media(site_id, id)

Deletes a specified survey media

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi(aqualink_sdk.ApiClient(configuration))
site_id = 1.2 # float | 
id = 1.2 # float | 

try:
    # Deletes a specified survey media
    api_instance.surveys_controller_delete_media(site_id, id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_find**
> list[Survey] surveys_controller_find(site_id)

Returns all site's survey

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi()
site_id = 1.2 # float | 

try:
    # Returns all site's survey
    api_response = api_instance.surveys_controller_find(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->surveys_controller_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  | 

### Return type

[**list[Survey]**](Survey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_find_media**
> list[SurveyMedia] surveys_controller_find_media(site_id, id)

Returns all media of a specified survey

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi()
site_id = 1.2 # float | 
id = 1.2 # float | 

try:
    # Returns all media of a specified survey
    api_response = api_instance.surveys_controller_find_media(site_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->surveys_controller_find_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  | 
 **id** | **float**|  | 

### Return type

[**list[SurveyMedia]**](SurveyMedia.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_find_one**
> Survey surveys_controller_find_one(site_id, id)

Returns specified survey

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi()
site_id = 1.2 # float | 
id = 1.2 # float | 

try:
    # Returns specified survey
    api_response = api_instance.surveys_controller_find_one(site_id, id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_update**
> Survey surveys_controller_update(body, site_id, id)

Updates a specified survey

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi(aqualink_sdk.ApiClient(configuration))
body = aqualink_sdk.EditSurveyDto() # EditSurveyDto | 
site_id = 1.2 # float | 
id = 1.2 # float | 

try:
    # Updates a specified survey
    api_response = api_instance.surveys_controller_update(body, site_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->surveys_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditSurveyDto**](EditSurveyDto.md)|  | 
 **site_id** | **float**|  | 
 **id** | **float**|  | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_update_media**
> SurveyMedia surveys_controller_update_media(body, site_id, id)

Updates a specified survey media

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi(aqualink_sdk.ApiClient(configuration))
body = aqualink_sdk.EditSurveyMediaDto() # EditSurveyMediaDto | 
site_id = 1.2 # float | 
id = 1.2 # float | 

try:
    # Updates a specified survey media
    api_response = api_instance.surveys_controller_update_media(body, site_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->surveys_controller_update_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditSurveyMediaDto**](EditSurveyMediaDto.md)|  | 
 **site_id** | **float**|  | 
 **id** | **float**|  | 

### Return type

[**SurveyMedia**](SurveyMedia.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **surveys_controller_upload**
> str surveys_controller_upload(file, site_id)

Uploads a new survey media

### Example
```python
from __future__ import print_function
import time
import aqualink_sdk
from aqualink_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = aqualink_sdk.SurveysApi(aqualink_sdk.ApiClient(configuration))
file = 'file_example' # str | 
site_id = 1.2 # float | 

try:
    # Uploads a new survey media
    api_response = api_instance.surveys_controller_upload(file, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->surveys_controller_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **site_id** | **float**|  | 

### Return type

**str**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

