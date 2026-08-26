# aqualink_sdk.AiChatApi

All URIs are relative to *https://production-dot-ocean-systems.uc.r.appspot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_chat_controller_chat**](AiChatApi.md#ai_chat_controller_chat) | **POST** /ai-chat | Get AI assistance for coral reef monitoring


# **ai_chat_controller_chat**
> ai_chat_controller_chat()

Get AI assistance for coral reef monitoring

### Example


```python
import time
import aqualink_sdk
from aqualink_sdk.api import ai_chat_api
from pprint import pprint
# Defining the host is optional and defaults to https://production-dot-ocean-systems.uc.r.appspot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = aqualink_sdk.Configuration(
    host = "https://production-dot-ocean-systems.uc.r.appspot.com/api"
)


# Enter a context with an instance of the API client
with aqualink_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ai_chat_api.AiChatApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get AI assistance for coral reef monitoring
        api_instance.ai_chat_controller_chat()
    except aqualink_sdk.ApiException as e:
        print("Exception when calling AiChatApi->ai_chat_controller_chat: %s\n" % e)
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
**200** | AI response generated successfully |  -  |
**400** | Invalid request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

