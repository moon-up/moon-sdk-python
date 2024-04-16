# openapi_client.AaveApi

All URIs are relative to *https://beta.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**borrow**](AaveApi.md#borrow) | **POST** /aave/{name}/borrow | 
[**lend**](AaveApi.md#lend) | **POST** /aave/{name}/lend | 
[**repay**](AaveApi.md#repay) | **POST** /aave/{name}/repay | 
[**user_reserve_data**](AaveApi.md#user_reserve_data) | **POST** /aave/{name}/user-reserve-data | 


# **borrow**
> TransactionAPIResponse borrow(authorization, name, aave_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.aave_input import AaveInput
from openapi_client.models.transaction_api_response import TransactionAPIResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AaveApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    aave_input = openapi_client.AaveInput() # AaveInput | 

    try:
        api_response = api_instance.borrow(authorization, name, aave_input)
        print("The response of AaveApi->borrow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveApi->borrow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **aave_input** | [**AaveInput**](AaveInput.md)|  | 

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

# **lend**
> TransactionAPIResponse lend(authorization, name, aave_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.aave_input import AaveInput
from openapi_client.models.transaction_api_response import TransactionAPIResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AaveApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    aave_input = openapi_client.AaveInput() # AaveInput | 

    try:
        api_response = api_instance.lend(authorization, name, aave_input)
        print("The response of AaveApi->lend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveApi->lend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **aave_input** | [**AaveInput**](AaveInput.md)|  | 

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

# **repay**
> TransactionAPIResponse repay(authorization, name, aave_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.aave_input import AaveInput
from openapi_client.models.transaction_api_response import TransactionAPIResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AaveApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    aave_input = openapi_client.AaveInput() # AaveInput | 

    try:
        api_response = api_instance.repay(authorization, name, aave_input)
        print("The response of AaveApi->repay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveApi->repay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **aave_input** | [**AaveInput**](AaveInput.md)|  | 

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

# **user_reserve_data**
> AaveReservesAPIResponse user_reserve_data(authorization, name, aave_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.aave_input import AaveInput
from openapi_client.models.aave_reserves_api_response import AaveReservesAPIResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://beta.usemoon.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AaveApi(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    aave_input = openapi_client.AaveInput() # AaveInput | 

    try:
        api_response = api_instance.user_reserve_data(authorization, name, aave_input)
        print("The response of AaveApi->user_reserve_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AaveApi->user_reserve_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **aave_input** | [**AaveInput**](AaveInput.md)|  | 

### Return type

[**AaveReservesAPIResponse**](AaveReservesAPIResponse.md)

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

