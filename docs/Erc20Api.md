# openapi_client.Erc20Api

All URIs are relative to *https://vault-api.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allowance_erc20**](Erc20Api.md#allowance_erc20) | **POST** /erc20/{name}/allowance | 
[**approve_erc20**](Erc20Api.md#approve_erc20) | **POST** /erc20/{name}/approve | 
[**balance_of_erc20**](Erc20Api.md#balance_of_erc20) | **POST** /erc20/{name}/balance-of | 
[**decimals_erc20**](Erc20Api.md#decimals_erc20) | **POST** /erc20/{name}/decimals | 
[**name_erc20**](Erc20Api.md#name_erc20) | **POST** /erc20/{name}/name | 
[**symbol_erc20**](Erc20Api.md#symbol_erc20) | **POST** /erc20/{name}/symbol | 
[**total_supply_erc20**](Erc20Api.md#total_supply_erc20) | **POST** /erc20/{name}/total-supply | 
[**transfer_erc20**](Erc20Api.md#transfer_erc20) | **POST** /erc20/{name}/transfer | 
[**transfer_from_erc20**](Erc20Api.md#transfer_from_erc20) | **POST** /erc20/{name}/transfer-from | 


# **allowance_erc20**
> AccountControllerResponse allowance_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.allowance_erc20(authorization, name, input_body)
        print("The response of Erc20Api->allowance_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->allowance_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

# **approve_erc20**
> AccountControllerResponse approve_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.approve_erc20(authorization, name, input_body)
        print("The response of Erc20Api->approve_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->approve_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

# **balance_of_erc20**
> AccountControllerResponse balance_of_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.balance_of_erc20(authorization, name, input_body)
        print("The response of Erc20Api->balance_of_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->balance_of_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

# **decimals_erc20**
> AccountControllerResponse decimals_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.decimals_erc20(authorization, name, input_body)
        print("The response of Erc20Api->decimals_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->decimals_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

# **name_erc20**
> AccountControllerResponse name_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.name_erc20(authorization, name, input_body)
        print("The response of Erc20Api->name_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->name_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

# **symbol_erc20**
> AccountControllerResponse symbol_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.symbol_erc20(authorization, name, input_body)
        print("The response of Erc20Api->symbol_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->symbol_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

# **total_supply_erc20**
> AccountControllerResponse total_supply_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.total_supply_erc20(authorization, name, input_body)
        print("The response of Erc20Api->total_supply_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->total_supply_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

# **transfer_erc20**
> AccountControllerResponse transfer_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.transfer_erc20(authorization, name, input_body)
        print("The response of Erc20Api->transfer_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->transfer_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

# **transfer_from_erc20**
> AccountControllerResponse transfer_from_erc20(authorization, name, input_body)



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
    api_instance = openapi_client.Erc20Api(api_client)
    authorization = 'authorization_example' # str | 
    name = 'name_example' # str | 
    input_body = openapi_client.InputBody() # InputBody | 

    try:
        api_response = api_instance.transfer_from_erc20(authorization, name, input_body)
        print("The response of Erc20Api->transfer_from_erc20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Erc20Api->transfer_from_erc20: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**|  | 
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

