# moonsdk.ConveyorFinanceApi

All URIs are relative to *https://beta.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**swap**](ConveyorFinanceApi.md#swap) | **POST** /conveyorfinance/{name}/swap | 


# **swap**
> ConveyorFinanceControllerResponse swap(authorization, name, token_swap_params)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.conveyor_finance_controller_response import ConveyorFinanceControllerResponse
from moonsdk.models.token_swap_params import TokenSwapParams
from moonsdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = moonsdk.Configuration(
    host = "https://beta.usemoon.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with moonsdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moonsdk.ConveyorFinanceApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    token_swap_params = moonsdk.TokenSwapParams() # TokenSwapParams | 

    try:
        api_response = await api_instance.swap(authorization, name, token_swap_params)
        print("The response of ConveyorFinanceApi->swap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConveyorFinanceApi->swap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **token_swap_params** | [**TokenSwapParams**](TokenSwapParams.md)|  | 

### Return type

[**ConveyorFinanceControllerResponse**](ConveyorFinanceControllerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

