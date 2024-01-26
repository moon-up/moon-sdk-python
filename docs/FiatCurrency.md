# FiatCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** |  | 
**symbol** | **str** |  | 
**name** | **str** |  | 
**code** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from moonsdk.models.fiat_currency import FiatCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FiatCurrency from a JSON string
fiat_currency_instance = FiatCurrency.from_json(json)
# print the JSON string representation of the object
print FiatCurrency.to_json()

# convert the object into a dict
fiat_currency_dict = fiat_currency_instance.to_dict()
# create an instance of FiatCurrency from a dict
fiat_currency_form_dict = fiat_currency.from_dict(fiat_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


