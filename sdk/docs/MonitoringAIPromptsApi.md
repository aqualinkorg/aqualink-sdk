# aqualink_sdk.MonitoringAIPromptsApi

All URIs are relative to *https://production-dot-ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prompts_controller_get_all_prompts**](MonitoringAIPromptsApi.md#prompts_controller_get_all_prompts) | **GET** /monitoring/prompts | Get all AI prompts
[**prompts_controller_get_prompt**](MonitoringAIPromptsApi.md#prompts_controller_get_prompt) | **GET** /monitoring/prompts/{promptKey} | Get a specific AI prompt by key
[**prompts_controller_get_prompt_history**](MonitoringAIPromptsApi.md#prompts_controller_get_prompt_history) | **GET** /monitoring/prompts/{promptKey}/history | Get version history for a prompt
[**prompts_controller_refresh_cache**](MonitoringAIPromptsApi.md#prompts_controller_refresh_cache) | **POST** /monitoring/prompts/cache/refresh | Refresh prompt cache manually
[**prompts_controller_rollback_to_version**](MonitoringAIPromptsApi.md#prompts_controller_rollback_to_version) | **POST** /monitoring/prompts/{promptKey}/rollback | Rollback a prompt to a previous version
[**prompts_controller_update_prompt**](MonitoringAIPromptsApi.md#prompts_controller_update_prompt) | **PUT** /monitoring/prompts/{promptKey} | Update an AI prompt


# **prompts_controller_get_all_prompts**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] prompts_controller_get_all_prompts()

Get all AI prompts

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring___ai_prompts_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring___ai_prompts_api.MonitoringAIPromptsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all AI prompts
        api_response = api_instance.prompts_controller_get_all_prompts()
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringAIPromptsApi->prompts_controller_get_all_prompts: %s\n" % e)
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

# **prompts_controller_get_prompt**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} prompts_controller_get_prompt(prompt_key)

Get a specific AI prompt by key

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring___ai_prompts_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring___ai_prompts_api.MonitoringAIPromptsApi(api_client)
    prompt_key = "promptKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a specific AI prompt by key
        api_response = api_instance.prompts_controller_get_prompt(prompt_key)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringAIPromptsApi->prompts_controller_get_prompt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_key** | **str**|  |

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

# **prompts_controller_get_prompt_history**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] prompts_controller_get_prompt_history(prompt_key)

Get version history for a prompt

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring___ai_prompts_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring___ai_prompts_api.MonitoringAIPromptsApi(api_client)
    prompt_key = "promptKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get version history for a prompt
        api_response = api_instance.prompts_controller_get_prompt_history(prompt_key)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringAIPromptsApi->prompts_controller_get_prompt_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_key** | **str**|  |

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

# **prompts_controller_refresh_cache**
> prompts_controller_refresh_cache()

Refresh prompt cache manually

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring___ai_prompts_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring___ai_prompts_api.MonitoringAIPromptsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Refresh prompt cache manually
        api_instance.prompts_controller_refresh_cache()
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringAIPromptsApi->prompts_controller_refresh_cache: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **prompts_controller_rollback_to_version**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} prompts_controller_rollback_to_version(prompt_key)

Rollback a prompt to a previous version

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring___ai_prompts_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring___ai_prompts_api.MonitoringAIPromptsApi(api_client)
    prompt_key = "promptKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Rollback a prompt to a previous version
        api_response = api_instance.prompts_controller_rollback_to_version(prompt_key)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringAIPromptsApi->prompts_controller_rollback_to_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_key** | **str**|  |

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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prompts_controller_update_prompt**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} prompts_controller_update_prompt(prompt_key)

Update an AI prompt

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import monitoring___ai_prompts_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring___ai_prompts_api.MonitoringAIPromptsApi(api_client)
    prompt_key = "promptKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update an AI prompt
        api_response = api_instance.prompts_controller_update_prompt(prompt_key)
        pprint(api_response)
    except aqualink_sdk.ApiException as e:
        print("Exception when calling MonitoringAIPromptsApi->prompts_controller_update_prompt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_key** | **str**|  |

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

