# moonsdk.YearnApi

All URIs are relative to *https://moon-vault-api-git-ew-supabase-migration-moonup.vercel.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_liquidity**](YearnApi.md#add_liquidity) | **POST** /yearn/{name}/add-liquidity | 
[**add_liquidity_weth**](YearnApi.md#add_liquidity_weth) | **POST** /yearn/{name}/add-liquidity-weth | 
[**remove_liquidity**](YearnApi.md#remove_liquidity) | **POST** /yearn/{name}/remove-liquidity | 
[**remove_liquidity_weth**](YearnApi.md#remove_liquidity_weth) | **POST** /yearn/{name}/remove-liquidity-weth | 


# **add_liquidity**
> TransactionAPIResponse add_liquidity(authorization, name, input_body)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import time
import os
import moonsdk
from moonsdk.models.input_body import InputBody
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.YearnApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = moonsdk.InputBody() # InputBody | 

    try:
        api_response = await api_instance.add_liquidity(authorization, name, input_body)
        print("The response of YearnApi->add_liquidity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YearnApi->add_liquidity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **input_body** | [**InputBody**](InputBody.md)|  | 

### Return type

[**TransactionAPIResponse**](TransactionAPIResponse.md)

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

# **add_liquidity_weth**
> TransactionAPIResponse add_liquidity_weth(authorization, name, input_body)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import time
import os
import moonsdk
from moonsdk.models.input_body import InputBody
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.YearnApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = moonsdk.InputBody() # InputBody | 

    try:
        api_response = await api_instance.add_liquidity_weth(authorization, name, input_body)
        print("The response of YearnApi->add_liquidity_weth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YearnApi->add_liquidity_weth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **input_body** | [**InputBody**](InputBody.md)|  | 

### Return type

[**TransactionAPIResponse**](TransactionAPIResponse.md)

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

# **remove_liquidity**
> TransactionAPIResponse remove_liquidity(authorization, name, input_body)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import time
import os
import moonsdk
from moonsdk.models.input_body import InputBody
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.YearnApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = moonsdk.InputBody() # InputBody | 

    try:
        api_response = await api_instance.remove_liquidity(authorization, name, input_body)
        print("The response of YearnApi->remove_liquidity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YearnApi->remove_liquidity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **input_body** | [**InputBody**](InputBody.md)|  | 

### Return type

[**TransactionAPIResponse**](TransactionAPIResponse.md)

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

# **remove_liquidity_weth**
> TransactionAPIResponse remove_liquidity_weth(authorization, name, input_body)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import time
import os
import moonsdk
from moonsdk.models.input_body import InputBody
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.YearnApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = moonsdk.InputBody() # InputBody | 

    try:
        api_response = await api_instance.remove_liquidity_weth(authorization, name, input_body)
        print("The response of YearnApi->remove_liquidity_weth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YearnApi->remove_liquidity_weth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **input_body** | [**InputBody**](InputBody.md)|  | 

### Return type

[**TransactionAPIResponse**](TransactionAPIResponse.md)

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

