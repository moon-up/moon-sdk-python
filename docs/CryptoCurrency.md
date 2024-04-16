# CryptoCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_display_name** | **str** |  | 
**icon** | **str** |  | 
**chain_id** | **float** |  | 
**address** | **str** |  | 
**decimals** | **float** |  | 
**network** | **str** |  | 
**symbol** | **str** |  | 
**name** | **str** |  | 
**code** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from openapi_client.models.crypto_currency import CryptoCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoCurrency from a JSON string
crypto_currency_instance = CryptoCurrency.from_json(json)
# print the JSON string representation of the object
print(CryptoCurrency.to_json())

# convert the object into a dict
crypto_currency_dict = crypto_currency_instance.to_dict()
# create an instance of CryptoCurrency from a dict
crypto_currency_form_dict = crypto_currency.from_dict(crypto_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


