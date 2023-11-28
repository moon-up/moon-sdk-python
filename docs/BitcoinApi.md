# openapi_client.BitcoinApi

All URIs are relative to *https://vault-api.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bitcoin_account**](BitcoinApi.md#create_bitcoin_account) | **POST** /bitcoin | 
[**get_bitcoin_account**](BitcoinApi.md#get_bitcoin_account) | **GET** /bitcoin/{accountName} | 
[**list_bitcoin_accounts**](BitcoinApi.md#list_bitcoin_accounts) | **GET** /bitcoin | 
[**sign_bitcoin_transaction**](BitcoinApi.md#sign_bitcoin_transaction) | **POST** /bitcoin/{accountName}/sign-tx | 


# **create_bitcoin_account**
> AccountControllerResponse create_bitcoin_account(authorization, bitcoin_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.account_controller_response import AccountControllerResponse
from openapi_client.models.bitcoin_input import BitcoinInput
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
    api_instance = openapi_client.BitcoinApi(api_client)
    authorization = 'authorization_example' # str | 
    bitcoin_input = openapi_client.BitcoinInput() # BitcoinInput | 

    try:
        api_response = api_instance.create_bitcoin_account(authorization, bitcoin_input)
        print("The response of BitcoinApi->create_bitcoin_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BitcoinApi->create_bitcoin_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **bitcoin_input** | [**BitcoinInput**](BitcoinInput.md)|  | 

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

# **get_bitcoin_account**
> AccountControllerResponse get_bitcoin_account(authorization, account_name)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.account_controller_response import AccountControllerResponse
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
    api_instance = openapi_client.BitcoinApi(api_client)
    authorization = 'authorization_example' # str | 
    account_name = 'account_name_example' # str | 

    try:
        api_response = api_instance.get_bitcoin_account(authorization, account_name)
        print("The response of BitcoinApi->get_bitcoin_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BitcoinApi->get_bitcoin_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **account_name** | **str**|  | 

### Return type

[**AccountControllerResponse**](AccountControllerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bitcoin_accounts**
> AccountControllerResponse list_bitcoin_accounts(authorization)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.account_controller_response import AccountControllerResponse
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
    api_instance = openapi_client.BitcoinApi(api_client)
    authorization = 'authorization_example' # str | 

    try:
        api_response = api_instance.list_bitcoin_accounts(authorization)
        print("The response of BitcoinApi->list_bitcoin_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BitcoinApi->list_bitcoin_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

### Return type

[**AccountControllerResponse**](AccountControllerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_bitcoin_transaction**
> AccountControllerResponse sign_bitcoin_transaction(authorization, account_name, bitcoin_transaction_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.account_controller_response import AccountControllerResponse
from openapi_client.models.bitcoin_transaction_input import BitcoinTransactionInput
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
    api_instance = openapi_client.BitcoinApi(api_client)
    authorization = 'authorization_example' # str | 
    account_name = 'account_name_example' # str | 
    bitcoin_transaction_input = openapi_client.BitcoinTransactionInput() # BitcoinTransactionInput | 

    try:
        api_response = api_instance.sign_bitcoin_transaction(authorization, account_name, bitcoin_transaction_input)
        print("The response of BitcoinApi->sign_bitcoin_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BitcoinApi->sign_bitcoin_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **account_name** | **str**|  | 
 **bitcoin_transaction_input** | [**BitcoinTransactionInput**](BitcoinTransactionInput.md)|  | 

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

