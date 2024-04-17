# moonsdk.OnramperApi

All URIs are relative to *https://beta.usemoon.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**on_ramper_checkout**](OnramperApi.md#on_ramper_checkout) | **POST** /onramper/fund/${accountName} | 
[**on_ramper_get_quotes_buy**](OnramperApi.md#on_ramper_get_quotes_buy) | **GET** /onramper/quotes/buy | 
[**on_ramper_get_quotes_sell**](OnramperApi.md#on_ramper_get_quotes_sell) | **GET** /onramper/quotes/sell | 
[**on_ramper_get_supported_assets**](OnramperApi.md#on_ramper_get_supported_assets) | **GET** /onramper/assets | 
[**on_ramper_get_supported_currencies**](OnramperApi.md#on_ramper_get_supported_currencies) | **GET** /onramper/currencies | 
[**on_ramper_get_supported_defaults_all**](OnramperApi.md#on_ramper_get_supported_defaults_all) | **GET** /onramper/defaults | 
[**on_ramper_get_supported_on_ramps_all**](OnramperApi.md#on_ramper_get_supported_on_ramps_all) | **GET** /onramper/onramps | 
[**on_ramper_get_supported_payment_types**](OnramperApi.md#on_ramper_get_supported_payment_types) | **GET** /onramper/payment-types | 
[**on_ramper_get_supported_payment_types_fiat**](OnramperApi.md#on_ramper_get_supported_payment_types_fiat) | **GET** /onramper/payment-types/fiat | 


# **on_ramper_checkout**
> object on_ramper_checkout(authorization, account_name, transaction_input)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.transaction_input import TransactionInput
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 
    account_name = 'account_name_example' # str | 
    transaction_input = moonsdk.TransactionInput() # TransactionInput | 

    try:
        api_response = await api_instance.on_ramper_checkout(authorization, account_name, transaction_input)
        print("The response of OnramperApi->on_ramper_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **account_name** | **str**|  | 
 **transaction_input** | [**TransactionInput**](TransactionInput.md)|  | 

### Return type

**object**

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

# **on_ramper_get_quotes_buy**
> List[Quote] on_ramper_get_quotes_buy(authorization, fiat, crypto, amount, payment_method=payment_method, uuid=uuid, client_name=client_name, country=country)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.quote import Quote
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 
    fiat = 'fiat_example' # str | 
    crypto = 'crypto_example' # str | 
    amount = 3.4 # float | 
    payment_method = 'creditcard' # str |  (optional) (default to 'creditcard')
    uuid = '' # str |  (optional) (default to '')
    client_name = '' # str |  (optional) (default to '')
    country = '' # str |  (optional) (default to '')

    try:
        api_response = await api_instance.on_ramper_get_quotes_buy(authorization, fiat, crypto, amount, payment_method=payment_method, uuid=uuid, client_name=client_name, country=country)
        print("The response of OnramperApi->on_ramper_get_quotes_buy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_get_quotes_buy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **fiat** | **str**|  | 
 **crypto** | **str**|  | 
 **amount** | **float**|  | 
 **payment_method** | **str**|  | [optional] [default to &#39;creditcard&#39;]
 **uuid** | **str**|  | [optional] [default to &#39;&#39;]
 **client_name** | **str**|  | [optional] [default to &#39;&#39;]
 **country** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[Quote]**](Quote.md)

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

# **on_ramper_get_quotes_sell**
> List[SellQuote] on_ramper_get_quotes_sell(authorization, fiat, crypto, amount, payment_method=payment_method, uuid=uuid, client_name=client_name, country=country)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.sell_quote import SellQuote
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 
    fiat = 'fiat_example' # str | 
    crypto = 'crypto_example' # str | 
    amount = 3.4 # float | 
    payment_method = 'creditcard' # str |  (optional) (default to 'creditcard')
    uuid = '' # str |  (optional) (default to '')
    client_name = '' # str |  (optional) (default to '')
    country = '' # str |  (optional) (default to '')

    try:
        api_response = await api_instance.on_ramper_get_quotes_sell(authorization, fiat, crypto, amount, payment_method=payment_method, uuid=uuid, client_name=client_name, country=country)
        print("The response of OnramperApi->on_ramper_get_quotes_sell:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_get_quotes_sell: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **fiat** | **str**|  | 
 **crypto** | **str**|  | 
 **amount** | **float**|  | 
 **payment_method** | **str**|  | [optional] [default to &#39;creditcard&#39;]
 **uuid** | **str**|  | [optional] [default to &#39;&#39;]
 **client_name** | **str**|  | [optional] [default to &#39;&#39;]
 **country** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[SellQuote]**](SellQuote.md)

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

# **on_ramper_get_supported_assets**
> SupportedAssetResponse on_ramper_get_supported_assets(authorization, source, country)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.supported_asset_response import SupportedAssetResponse
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 
    source = 'source_example' # str | 
    country = 'country_example' # str | 

    try:
        api_response = await api_instance.on_ramper_get_supported_assets(authorization, source, country)
        print("The response of OnramperApi->on_ramper_get_supported_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_get_supported_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **source** | **str**|  | 
 **country** | **str**|  | 

### Return type

[**SupportedAssetResponse**](SupportedAssetResponse.md)

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

# **on_ramper_get_supported_currencies**
> SupportedCurrenciesResponse on_ramper_get_supported_currencies(authorization, type)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.supported_currencies_response import SupportedCurrenciesResponse
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 
    type = 'type_example' # str | 

    try:
        api_response = await api_instance.on_ramper_get_supported_currencies(authorization, type)
        print("The response of OnramperApi->on_ramper_get_supported_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_get_supported_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **type** | **str**|  | 

### Return type

[**SupportedCurrenciesResponse**](SupportedCurrenciesResponse.md)

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

# **on_ramper_get_supported_defaults_all**
> SupportedDefaultResponse on_ramper_get_supported_defaults_all(authorization, country, type)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.supported_default_response import SupportedDefaultResponse
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 
    country = 'country_example' # str | 
    type = 'type_example' # str | 

    try:
        api_response = await api_instance.on_ramper_get_supported_defaults_all(authorization, country, type)
        print("The response of OnramperApi->on_ramper_get_supported_defaults_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_get_supported_defaults_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **country** | **str**|  | 
 **type** | **str**|  | 

### Return type

[**SupportedDefaultResponse**](SupportedDefaultResponse.md)

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

# **on_ramper_get_supported_on_ramps_all**
> GetSupportedOnRampsResponse on_ramper_get_supported_on_ramps_all(authorization)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.get_supported_on_ramps_response import GetSupportedOnRampsResponse
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 

    try:
        api_response = await api_instance.on_ramper_get_supported_on_ramps_all(authorization)
        print("The response of OnramperApi->on_ramper_get_supported_on_ramps_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_get_supported_on_ramps_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

### Return type

[**GetSupportedOnRampsResponse**](GetSupportedOnRampsResponse.md)

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

# **on_ramper_get_supported_payment_types**
> SupportedPaymentTypesCurrencyResponse on_ramper_get_supported_payment_types(authorization, fiat, country, type)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.supported_payment_types_currency_response import SupportedPaymentTypesCurrencyResponse
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 
    fiat = 'fiat_example' # str | 
    country = 'country_example' # str | 
    type = 'type_example' # str | 

    try:
        api_response = await api_instance.on_ramper_get_supported_payment_types(authorization, fiat, country, type)
        print("The response of OnramperApi->on_ramper_get_supported_payment_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_get_supported_payment_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **fiat** | **str**|  | 
 **country** | **str**|  | 
 **type** | **str**|  | 

### Return type

[**SupportedPaymentTypesCurrencyResponse**](SupportedPaymentTypesCurrencyResponse.md)

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

# **on_ramper_get_supported_payment_types_fiat**
> SupportedPaymentTypesCurrencyResponse on_ramper_get_supported_payment_types_fiat(authorization, fiat, country)



### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (BearerAuth):

```python
import moonsdk
from moonsdk.models.supported_payment_types_currency_response import SupportedPaymentTypesCurrencyResponse
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
    api_instance = moonsdk.OnramperApi(api_client)
    authorization = 'authorization_example' # str | 
    fiat = 'fiat_example' # str | 
    country = 'country_example' # str | 

    try:
        api_response = await api_instance.on_ramper_get_supported_payment_types_fiat(authorization, fiat, country)
        print("The response of OnramperApi->on_ramper_get_supported_payment_types_fiat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnramperApi->on_ramper_get_supported_payment_types_fiat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **fiat** | **str**|  | 
 **country** | **str**|  | 

### Return type

[**SupportedPaymentTypesCurrencyResponse**](SupportedPaymentTypesCurrencyResponse.md)

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

