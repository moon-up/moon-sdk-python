# moonsdk.DogeCoinApi

All URIs are relative to *https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_doge_coin_account**](DogeCoinApi.md#create_doge_coin_account) | **POST** /dogecoin | 
[**get_doge_coin_account**](DogeCoinApi.md#get_doge_coin_account) | **GET** /dogecoin/{accountName} | 
[**list_doge_coin_accounts**](DogeCoinApi.md#list_doge_coin_accounts) | **GET** /dogecoin | 
[**sign_doge_coin_transaction**](DogeCoinApi.md#sign_doge_coin_transaction) | **POST** /dogecoin/{accountName}/sign-tx | 


# **create_doge_coin_account**
> AccountAPIResponse create_doge_coin_account(authorization, doge_coin_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import time
import os
import moonsdk
from moonsdk.models.account_api_response import AccountAPIResponse
from moonsdk.models.doge_coin_input import DogeCoinInput
from moonsdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app
# See configuration.py for a list of all supported configuration parameters.
configuration = moonsdk.Configuration(
    host = "https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app"
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
    api_instance = moonsdk.DogeCoinApi(api_client)
    authorization = 'authorization_example' # str | 
    doge_coin_input = moonsdk.DogeCoinInput() # DogeCoinInput | 

    try:
        api_response = await api_instance.create_doge_coin_account(authorization, doge_coin_input)
        print("The response of DogeCoinApi->create_doge_coin_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DogeCoinApi->create_doge_coin_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **doge_coin_input** | [**DogeCoinInput**](DogeCoinInput.md)|  | 

### Return type

[**AccountAPIResponse**](AccountAPIResponse.md)

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

# **get_doge_coin_account**
> AccountAPIResponse get_doge_coin_account(authorization, account_name)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import time
import os
import moonsdk
from moonsdk.models.account_api_response import AccountAPIResponse
from moonsdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app
# See configuration.py for a list of all supported configuration parameters.
configuration = moonsdk.Configuration(
    host = "https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app"
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
    api_instance = moonsdk.DogeCoinApi(api_client)
    authorization = 'authorization_example' # str | 
    account_name = 'account_name_example' # str | 

    try:
        api_response = await api_instance.get_doge_coin_account(authorization, account_name)
        print("The response of DogeCoinApi->get_doge_coin_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DogeCoinApi->get_doge_coin_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **account_name** | **str**|  | 

### Return type

[**AccountAPIResponse**](AccountAPIResponse.md)

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

# **list_doge_coin_accounts**
> AccountAPIResponse list_doge_coin_accounts(authorization)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import time
import os
import moonsdk
from moonsdk.models.account_api_response import AccountAPIResponse
from moonsdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app
# See configuration.py for a list of all supported configuration parameters.
configuration = moonsdk.Configuration(
    host = "https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app"
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
    api_instance = moonsdk.DogeCoinApi(api_client)
    authorization = 'authorization_example' # str | 

    try:
        api_response = await api_instance.list_doge_coin_accounts(authorization)
        print("The response of DogeCoinApi->list_doge_coin_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DogeCoinApi->list_doge_coin_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

### Return type

[**AccountAPIResponse**](AccountAPIResponse.md)

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

# **sign_doge_coin_transaction**
> DogeCoinAPIResponse sign_doge_coin_transaction(authorization, account_name, doge_coin_transaction_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import time
import os
import moonsdk
from moonsdk.models.doge_coin_api_response import DogeCoinAPIResponse
from moonsdk.models.doge_coin_transaction_input import DogeCoinTransactionInput
from moonsdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app
# See configuration.py for a list of all supported configuration parameters.
configuration = moonsdk.Configuration(
    host = "https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app"
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
    api_instance = moonsdk.DogeCoinApi(api_client)
    authorization = 'authorization_example' # str | 
    account_name = 'account_name_example' # str | 
    doge_coin_transaction_input = moonsdk.DogeCoinTransactionInput() # DogeCoinTransactionInput | 

    try:
        api_response = await api_instance.sign_doge_coin_transaction(authorization, account_name, doge_coin_transaction_input)
        print("The response of DogeCoinApi->sign_doge_coin_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DogeCoinApi->sign_doge_coin_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **account_name** | **str**|  | 
 **doge_coin_transaction_input** | [**DogeCoinTransactionInput**](DogeCoinTransactionInput.md)|  | 

### Return type

[**DogeCoinAPIResponse**](DogeCoinAPIResponse.md)

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

