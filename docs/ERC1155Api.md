# moonsdk.ERC1155Api

All URIs are relative to *https://beta.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_of**](ERC1155Api.md#balance_of) | **POST** /erc1155/{name}/balance-of | 
[**balance_of_batch**](ERC1155Api.md#balance_of_batch) | **POST** /erc1155/{name}/balance-of-batch | 
[**is_approved_for_all**](ERC1155Api.md#is_approved_for_all) | **POST** /erc1155/{name}/is-approved-for-all | 
[**safe_batch_transfer_from**](ERC1155Api.md#safe_batch_transfer_from) | **POST** /erc1155/{name}/safe-batch-transfer-from | 
[**safe_transfer_from**](ERC1155Api.md#safe_transfer_from) | **POST** /erc1155/{name}/safe-transfer-from | 
[**set_approval_for_all**](ERC1155Api.md#set_approval_for_all) | **POST** /erc1155/{name}/set-approval-for-all | 


# **balance_of**
> TransactionAPIResponse balance_of(name, authorization, erc1155_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.erc1155_request import Erc1155Request
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.ERC1155Api(api_client)
    name = 'name_example' # str | 
    authorization = 'authorization_example' # str | 
    erc1155_request = moonsdk.Erc1155Request() # Erc1155Request | 

    try:
        api_response = await api_instance.balance_of(name, authorization, erc1155_request)
        print("The response of ERC1155Api->balance_of:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ERC1155Api->balance_of: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization** | **str**|  | 
 **erc1155_request** | [**Erc1155Request**](Erc1155Request.md)|  | 

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

# **balance_of_batch**
> TransactionAPIResponse balance_of_batch(name, authorization, erc1155_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.erc1155_request import Erc1155Request
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.ERC1155Api(api_client)
    name = 'name_example' # str | 
    authorization = 'authorization_example' # str | 
    erc1155_request = moonsdk.Erc1155Request() # Erc1155Request | 

    try:
        api_response = await api_instance.balance_of_batch(name, authorization, erc1155_request)
        print("The response of ERC1155Api->balance_of_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ERC1155Api->balance_of_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization** | **str**|  | 
 **erc1155_request** | [**Erc1155Request**](Erc1155Request.md)|  | 

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

# **is_approved_for_all**
> TransactionAPIResponse is_approved_for_all(name, authorization, erc1155_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.erc1155_request import Erc1155Request
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.ERC1155Api(api_client)
    name = 'name_example' # str | 
    authorization = 'authorization_example' # str | 
    erc1155_request = moonsdk.Erc1155Request() # Erc1155Request | 

    try:
        api_response = await api_instance.is_approved_for_all(name, authorization, erc1155_request)
        print("The response of ERC1155Api->is_approved_for_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ERC1155Api->is_approved_for_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization** | **str**|  | 
 **erc1155_request** | [**Erc1155Request**](Erc1155Request.md)|  | 

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

# **safe_batch_transfer_from**
> TransactionAPIResponse safe_batch_transfer_from(name, authorization, erc1155_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.erc1155_request import Erc1155Request
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.ERC1155Api(api_client)
    name = 'name_example' # str | 
    authorization = 'authorization_example' # str | 
    erc1155_request = moonsdk.Erc1155Request() # Erc1155Request | 

    try:
        api_response = await api_instance.safe_batch_transfer_from(name, authorization, erc1155_request)
        print("The response of ERC1155Api->safe_batch_transfer_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ERC1155Api->safe_batch_transfer_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization** | **str**|  | 
 **erc1155_request** | [**Erc1155Request**](Erc1155Request.md)|  | 

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

# **safe_transfer_from**
> TransactionAPIResponse safe_transfer_from(name, authorization, erc1155_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.erc1155_request import Erc1155Request
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.ERC1155Api(api_client)
    name = 'name_example' # str | 
    authorization = 'authorization_example' # str | 
    erc1155_request = moonsdk.Erc1155Request() # Erc1155Request | 

    try:
        api_response = await api_instance.safe_transfer_from(name, authorization, erc1155_request)
        print("The response of ERC1155Api->safe_transfer_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ERC1155Api->safe_transfer_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization** | **str**|  | 
 **erc1155_request** | [**Erc1155Request**](Erc1155Request.md)|  | 

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

# **set_approval_for_all**
> TransactionAPIResponse set_approval_for_all(name, authorization, erc1155_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.erc1155_request import Erc1155Request
from moonsdk.models.transaction_api_response import TransactionAPIResponse
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
    api_instance = moonsdk.ERC1155Api(api_client)
    name = 'name_example' # str | 
    authorization = 'authorization_example' # str | 
    erc1155_request = moonsdk.Erc1155Request() # Erc1155Request | 

    try:
        api_response = await api_instance.set_approval_for_all(name, authorization, erc1155_request)
        print("The response of ERC1155Api->set_approval_for_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ERC1155Api->set_approval_for_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization** | **str**|  | 
 **erc1155_request** | [**Erc1155Request**](Erc1155Request.md)|  | 

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

