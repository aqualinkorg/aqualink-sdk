# aqualink_sdk.MonitoringApi

All URIs are relative to *https://production-dot-ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitoring_controller_get_monitoring_last_month**](MonitoringApi.md#monitoring_controller_get_monitoring_last_month) | **GET** /monitoring/last-month | Get monitoring metrics for last month for each site with a spotter
[**monitoring_controller_get_monitoring_stats**](MonitoringApi.md#monitoring_controller_get_monitoring_stats) | **GET** /monitoring | Get usage metrics
[**monitoring_controller_get_sites_overview**](MonitoringApi.md#monitoring_controller_get_sites_overview) | **GET** /monitoring/sites-overview | Get Aqualink overview
[**monitoring_controller_get_sites_status**](MonitoringApi.md#monitoring_controller_get_sites_status) | **GET** /monitoring/sites-status | Get sites&#39; status
[**monitoring_controller_get_surveys_report**](MonitoringApi.md#monitoring_controller_get_surveys_report) | **GET** /monitoring/surveys-report | Get surveys report
[**monitoring_controller_post_monitoring_metric**](MonitoringApi.md#monitoring_controller_post_monitoring_metric) | **POST** /monitoring | Post a usage metric


# **monitoring_controller_get_monitoring_last_month**
> monitoring_controller_get_monitoring_last_month()

Get monitoring metrics for last month for each site with a spotter

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_api.MonitoringApi(api_client)
    csv = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get monitoring metrics for last month for each site with a spotter
        api_instance.monitoring_controller_get_monitoring_last_month(csv=csv)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringApi->monitoring_controller_get_monitoring_last_month: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv** | **bool**|  | [optional]

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitoring_controller_get_monitoring_stats**
> monitoring_controller_get_monitoring_stats()

Get usage metrics

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_api.MonitoringApi(api_client)
    site_ids = [1,3,5] # [float] |  (optional)
    spotter_id = "SPOT-2742" # str |  (optional)
    monthly = True # bool |  (optional)
    start = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    csv = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get usage metrics
        api_instance.monitoring_controller_get_monitoring_stats(site_ids=site_ids, spotter_id=spotter_id, monthly=monthly, start=start, end=end, csv=csv)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringApi->monitoring_controller_get_monitoring_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_ids** | **[float]**|  | [optional]
 **spotter_id** | **str**|  | [optional]
 **monthly** | **bool**|  | [optional]
 **start** | **datetime**|  | [optional]
 **end** | **datetime**|  | [optional]
 **csv** | **bool**|  | [optional]

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitoring_controller_get_sites_overview**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] monitoring_controller_get_sites_overview()

Get Aqualink overview

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_api.MonitoringApi(api_client)
    site_id = 42 # float |  (optional)
    site_name = "Bellows South Africa" # str |  (optional)
    spotter_id = "SPOT-2742" # str |  (optional)
    admin_email = "admin@example.com" # str |  (optional)
    admin_username = "John Smith" # str |  (optional)
    organization = "Aqualink" # str |  (optional)
    status = "deployed" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Aqualink overview
        api_response = api_instance.monitoring_controller_get_sites_overview(site_id=site_id, site_name=site_name, spotter_id=spotter_id, admin_email=admin_email, admin_username=admin_username, organization=organization, status=status)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringApi->monitoring_controller_get_sites_overview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **float**|  | [optional]
 **site_name** | **str**|  | [optional]
 **spotter_id** | **str**|  | [optional]
 **admin_email** | **str**|  | [optional]
 **admin_username** | **str**|  | [optional]
 **organization** | **str**|  | [optional]
 **status** | **str**|  | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **monitoring_controller_get_sites_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} monitoring_controller_get_sites_status()

Get sites' status

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_api.MonitoringApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get sites' status
        api_response = api_instance.monitoring_controller_get_sites_status()
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringApi->monitoring_controller_get_sites_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **monitoring_controller_get_surveys_report**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] monitoring_controller_get_surveys_report()

Get surveys report

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_api.MonitoringApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get surveys report
        api_response = api_instance.monitoring_controller_get_surveys_report()
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringApi->monitoring_controller_get_surveys_report: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **monitoring_controller_post_monitoring_metric**
> monitoring_controller_post_monitoring_metric(post_monitoring_metric_dto)

Post a usage metric

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring_api
from aqualink_sdk.model.post_monitoring_metric_dto import PostMonitoringMetricDto
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_api.MonitoringApi(api_client)
    post_monitoring_metric_dto = PostMonitoringMetricDto(
        metric="time_series_request",
        site_id=1,
    ) # PostMonitoringMetricDto | 

    # example passing only required values which don't have defaults set
    try:
        # Post a usage metric
        api_instance.monitoring_controller_post_monitoring_metric(post_monitoring_metric_dto)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringApi->monitoring_controller_post_monitoring_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_monitoring_metric_dto** | [**PostMonitoringMetricDto**](PostMonitoringMetricDto.md)|  |

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

