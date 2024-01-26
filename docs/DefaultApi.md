# moonsdk.DefaultApi

All URIs are relative to *https://vault-api.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message**](DefaultApi.md#get_message) | **GET** /ping | 


# **get_message**
> PingResponse get_message()



### Example


```python
import time
import os
import moonsdk
from moonsdk.models.ping_response import PingResponse
from moonsdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://vault-api.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = moonsdk.Configuration(
    host = "https://vault-api.usemoon.ai"
)


# Enter a context with an instance of the API client
async with moonsdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moonsdk.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_message()
        print("The response of DefaultApi->get_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_message: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

