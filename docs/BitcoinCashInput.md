# BitcoinCashInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.bitcoin_cash_input import BitcoinCashInput

# TODO update the JSON string below
json = "{}"
# create an instance of BitcoinCashInput from a JSON string
bitcoin_cash_input_instance = BitcoinCashInput.from_json(json)
# print the JSON string representation of the object
print BitcoinCashInput.to_json()

# convert the object into a dict
bitcoin_cash_input_dict = bitcoin_cash_input_instance.to_dict()
# create an instance of BitcoinCashInput from a dict
bitcoin_cash_input_form_dict = bitcoin_cash_input.from_dict(bitcoin_cash_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


