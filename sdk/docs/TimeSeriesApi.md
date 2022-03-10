# aqualink_sdk.TimeSeriesApi

All URIs are relative to *https://ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**time_series_controller_find_site_data**](TimeSeriesApi.md#time_series_controller_find_site_data) | **GET** /time-series/sites/{siteId} | Returns specified time series data for a specified site
[**time_series_controller_find_site_data_range**](TimeSeriesApi.md#time_series_controller_find_site_data_range) | **GET** /time-series/sites/{siteId}/range | Returns the range of the available time series data for a specified site
[**time_series_controller_find_survey_point_data**](TimeSeriesApi.md#time_series_controller_find_survey_point_data) | **GET** /time-series/sites/{siteId}/site-survey-points/{surveyPointId} | Returns specified time series data for a specified site point of interest
[**time_series_controller_find_survey_point_data_range**](TimeSeriesApi.md#time_series_controller_find_survey_point_data_range) | **GET** /time-series/sites/{siteId}/site-survey-points/{surveyPointId}/range | Returns the range of the available time series data for a specified site point of interest
[**time_series_controller_upload_time_series_data**](TimeSeriesApi.md#time_series_controller_upload_time_series_data) | **POST** /time-series/sites/{siteId}/site-survey-points/{surveyPointId}/upload | Upload time series data


# **time_series_controller_find_site_data**
> InlineResponse200 time_series_controller_find_site_data(site_id, metrics, start, end, hourly)

Returns specified time series data for a specified site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import time_series_api
from aqualink_sdk.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = time_series_api.TimeSeriesApi(api_client)
    site_id = 1 # float | 
    metrics = ["bottom_temperature","top_temperature"] # [str] | 
    start = "2021-05-18T10:20:28.017Z" # str | 
    end = "2021-05-18T10:20:28.017Z" # str | 
    hourly = False # bool | 

    # example passing only required values which don't have defaults set
    try:
        # Returns specified time series data for a specified site
        api_response = api_instance.time_series_controller_find_site_data(site_id, metrics, start, end, hourly)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling TimeSeriesApi->time_series_controller_find_site_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **metrics** | **[str]**|  |
 **start** | **str**|  |
 **end** | **str**|  |
 **hourly** | **bool**|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **time_series_controller_find_site_data_range**
> InlineResponse2001 time_series_controller_find_site_data_range(site_id)

Returns the range of the available time series data for a specified site

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import time_series_api
from aqualink_sdk.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = time_series_api.TimeSeriesApi(api_client)
    site_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns the range of the available time series data for a specified site
        api_response = api_instance.time_series_controller_find_site_data_range(site_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling TimeSeriesApi->time_series_controller_find_site_data_range: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **time_series_controller_find_survey_point_data**
> InlineResponse200 time_series_controller_find_survey_point_data(site_id, survey_point_id, metrics, start, end, hourly)

Returns specified time series data for a specified site point of interest

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import time_series_api
from aqualink_sdk.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = time_series_api.TimeSeriesApi(api_client)
    site_id = 1 # float | 
    survey_point_id = 1 # float | 
    metrics = ["bottom_temperature","top_temperature"] # [str] | 
    start = "2021-05-18T10:20:28.017Z" # str | 
    end = "2021-05-18T10:20:28.017Z" # str | 
    hourly = False # bool | 

    # example passing only required values which don't have defaults set
    try:
        # Returns specified time series data for a specified site point of interest
        api_response = api_instance.time_series_controller_find_survey_point_data(site_id, survey_point_id, metrics, start, end, hourly)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling TimeSeriesApi->time_series_controller_find_survey_point_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **survey_point_id** | **float**|  |
 **metrics** | **[str]**|  |
 **start** | **str**|  |
 **end** | **str**|  |
 **hourly** | **bool**|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **time_series_controller_find_survey_point_data_range**
> InlineResponse2001 time_series_controller_find_survey_point_data_range(site_id, survey_point_id)

Returns the range of the available time series data for a specified site point of interest

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import time_series_api
from aqualink_sdk.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = time_series_api.TimeSeriesApi(api_client)
    site_id = 1 # float | 
    survey_point_id = 1 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Returns the range of the available time series data for a specified site point of interest
        api_response = api_instance.time_series_controller_find_survey_point_data_range(site_id, survey_point_id)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling TimeSeriesApi->time_series_controller_find_survey_point_data_range: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **survey_point_id** | **float**|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **time_series_controller_upload_time_series_data**
> time_series_controller_upload_time_series_data(site_id, survey_point_id, fail_on_warning)

Upload time series data

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import time_series_api
from pprint import pprint
# Defining the host is optional and defaults to https://ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = time_series_api.TimeSeriesApi(api_client)
    site_id = 1 # float | 
    survey_point_id = 1 # float | 
    fail_on_warning = True # bool | 

    # example passing only required values which don't have defaults set
    try:
        # Upload time series data
        api_instance.time_series_controller_upload_time_series_data(site_id, survey_point_id, fail_on_warning)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling TimeSeriesApi->time_series_controller_upload_time_series_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  |
 **survey_point_id** | **float**|  |
 **fail_on_warning** | **bool**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

