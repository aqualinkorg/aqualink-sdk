# swagger_client.SitePointsOfInterestApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**site_survey_points_controller_create**](SitePointsOfInterestApi.md#site_survey_points_controller_create) | **POST** /site-survey-points | Creates a new site point of interest
[**site_survey_points_controller_delete**](SitePointsOfInterestApi.md#site_survey_points_controller_delete) | **DELETE** /site-survey-points/{id} | Deletes specified site point of interest
[**site_survey_points_controller_find**](SitePointsOfInterestApi.md#site_survey_points_controller_find) | **GET** /site-survey-points | Returns site points of interest filtered by the provided filters
[**site_survey_points_controller_find_one**](SitePointsOfInterestApi.md#site_survey_points_controller_find_one) | **GET** /site-survey-points/{id} | Returns specified site point of interest
[**site_survey_points_controller_update**](SitePointsOfInterestApi.md#site_survey_points_controller_update) | **PUT** /site-survey-points/{id} | Updates specified site point of interest

# **site_survey_points_controller_create**
> SiteSurveyPoint site_survey_points_controller_create(body)

Creates a new site point of interest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitePointsOfInterestApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSiteSurveyPointDto() # CreateSiteSurveyPointDto | 

try:
    # Creates a new site point of interest
    api_response = api_instance.site_survey_points_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitePointsOfInterestApi->site_survey_points_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSiteSurveyPointDto**](CreateSiteSurveyPointDto.md)|  | 

### Return type

[**SiteSurveyPoint**](SiteSurveyPoint.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_survey_points_controller_delete**
> site_survey_points_controller_delete(id)

Deletes specified site point of interest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitePointsOfInterestApi(swagger_client.ApiClient(configuration))
id = 1.2 # float | 

try:
    # Deletes specified site point of interest
    api_instance.site_survey_points_controller_delete(id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_survey_points_controller_find**
> list[SiteSurveyPoint] site_survey_points_controller_find(name=name, site_id=site_id)

Returns site points of interest filtered by the provided filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SitePointsOfInterestApi()
name = 'name_example' # str |  (optional)
site_id = 1.2 # float |  (optional)

try:
    # Returns site points of interest filtered by the provided filters
    api_response = api_instance.site_survey_points_controller_find(name=name, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitePointsOfInterestApi->site_survey_points_controller_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **site_id** | **float**|  | [optional] 

### Return type

[**list[SiteSurveyPoint]**](SiteSurveyPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_survey_points_controller_find_one**
> SiteSurveyPoint site_survey_points_controller_find_one(id)

Returns specified site point of interest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SitePointsOfInterestApi()
id = 1.2 # float | 

try:
    # Returns specified site point of interest
    api_response = api_instance.site_survey_points_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_survey_points_controller_update**
> SiteSurveyPoint site_survey_points_controller_update(body, id)

Updates specified site point of interest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SitePointsOfInterestApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateSiteSurveyPointDto() # UpdateSiteSurveyPointDto | 
id = 1.2 # float | 

try:
    # Updates specified site point of interest
    api_response = api_instance.site_survey_points_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitePointsOfInterestApi->site_survey_points_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSiteSurveyPointDto**](UpdateSiteSurveyPointDto.md)|  | 
 **id** | **float**|  | 

### Return type

[**SiteSurveyPoint**](SiteSurveyPoint.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

