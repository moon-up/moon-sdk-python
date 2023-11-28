# openapi_client.Erc4337Api

All URIs are relative to *https://vault-api.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address**](Erc4337Api.md#get_address) | **POST** /erc4337/{accountName}/address | 
[**sign_broadcast_user_op_tx**](Erc4337Api.md#sign_broadcast_user_op_tx) | **POST** /erc4337/{accountName}/sign-broadcast-userop-tx | 


# **get_address**
> AccountControllerResponse get_address(authorization, account_name, input_body)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.account_controller_response import AccountControllerResponse
from openapi_client.models.input_body import InputBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://vault-api.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://vault-api.usemoon.ai"
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Erc4337Api(api_client)
    authorization = 'authorization_example' # str | 
    account_name = 'account_name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.get_address(authorization, account_name, input_body)
        print("The response of Erc4337Api->get_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc4337Api->get_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **account_name** | **str**|  | 
 **input_body** | [**InputBody**](InputBody.md)|  | 

### Return type

[**AccountControllerResponse**](AccountControllerResponse.md)

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

# **sign_broadcast_user_op_tx**
> AccountControllerResponse sign_broadcast_user_op_tx(authorization, account_name, input_body)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.account_controller_response import AccountControllerResponse
from openapi_client.models.input_body import InputBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://vault-api.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://vault-api.usemoon.ai"
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Erc4337Api(api_client)
    authorization = 'authorization_example' # str | 
    account_name = 'account_name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.sign_broadcast_user_op_tx(authorization, account_name, input_body)
        print("The response of Erc4337Api->sign_broadcast_user_op_tx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc4337Api->sign_broadcast_user_op_tx: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **account_name** | **str**|  | 
 **input_body** | [**InputBody**](InputBody.md)|  | 

### Return type

[**AccountControllerResponse**](AccountControllerResponse.md)

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

