# openapi_client.Erc721Api

All URIs are relative to *https://beta.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve**](Erc721Api.md#approve) | **POST** /erc721/{name}/approve | 
[**balance_of**](Erc721Api.md#balance_of) | **POST** /erc721/{name}/balance-of | 
[**get_approved**](Erc721Api.md#get_approved) | **POST** /erc721/{name}/get-approved | 
[**is_approved_for_all**](Erc721Api.md#is_approved_for_all) | **POST** /erc721/{name}/is-approved-for-all | 
[**name**](Erc721Api.md#name) | **POST** /erc721/{name}/name | 
[**owner_of**](Erc721Api.md#owner_of) | **POST** /erc721/{name}/owner-of | 
[**safe_transfer_from**](Erc721Api.md#safe_transfer_from) | **POST** /erc721/{name}/safe-transfer-from | 
[**set_approval_for_all**](Erc721Api.md#set_approval_for_all) | **POST** /erc721/{name}/set-approval-for-all | 
[**symbol**](Erc721Api.md#symbol) | **POST** /erc721/{name}/symbol | 
[**token_uri**](Erc721Api.md#token_uri) | **POST** /erc721/{name}/token-uri | 
[**transfer**](Erc721Api.md#transfer) | **POST** /erc721/{name}/transfer | 
[**transfer_from**](Erc721Api.md#transfer_from) | **POST** /erc721/{name}/transfer-from | 


# **approve**
> TransactionAPIResponse approve(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.approve(authorization, name, erc721_request)
        print("The response of Erc721Api->approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

# **balance_of**
> TransactionAPIResponse balance_of(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.balance_of(authorization, name, erc721_request)
        print("The response of Erc721Api->balance_of:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->balance_of: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

# **get_approved**
> TransactionAPIResponse get_approved(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.get_approved(authorization, name, erc721_request)
        print("The response of Erc721Api->get_approved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->get_approved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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
> TransactionAPIResponse is_approved_for_all(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.is_approved_for_all(authorization, name, erc721_request)
        print("The response of Erc721Api->is_approved_for_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->is_approved_for_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

# **name**
> TransactionAPIResponse name(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.name(authorization, name, erc721_request)
        print("The response of Erc721Api->name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

# **owner_of**
> TransactionAPIResponse owner_of(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.owner_of(authorization, name, erc721_request)
        print("The response of Erc721Api->owner_of:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->owner_of: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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
> TransactionAPIResponse safe_transfer_from(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.safe_transfer_from(authorization, name, erc721_request)
        print("The response of Erc721Api->safe_transfer_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->safe_transfer_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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
> TransactionAPIResponse set_approval_for_all(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.set_approval_for_all(authorization, name, erc721_request)
        print("The response of Erc721Api->set_approval_for_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->set_approval_for_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

# **symbol**
> TransactionAPIResponse symbol(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.symbol(authorization, name, erc721_request)
        print("The response of Erc721Api->symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

# **token_uri**
> TransactionAPIResponse token_uri(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.token_uri(authorization, name, erc721_request)
        print("The response of Erc721Api->token_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->token_uri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

# **transfer**
> TransactionAPIResponse transfer(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.transfer(authorization, name, erc721_request)
        print("The response of Erc721Api->transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

# **transfer_from**
> TransactionAPIResponse transfer_from(authorization, name, erc721_request)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.erc721_request import Erc721Request
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
    api_instance = openapi_client.Erc721Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    erc721_request = openapi_client.Erc721Request() # Erc721Request | 

    try:
        api_response = api_instance.transfer_from(authorization, name, erc721_request)
        print("The response of Erc721Api->transfer_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc721Api->transfer_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
 **erc721_request** | [**Erc721Request**](Erc721Request.md)|  | 

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

