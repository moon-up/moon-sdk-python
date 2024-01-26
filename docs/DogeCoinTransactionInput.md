# DogeCoinTransactionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from moonsdk.models.doge_coin_transaction_input import DogeCoinTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of DogeCoinTransactionInput from a JSON string
doge_coin_transaction_input_instance = DogeCoinTransactionInput.from_json(json)
# print the JSON string representation of the object
print DogeCoinTransactionInput.to_json()

# convert the object into a dict
doge_coin_transaction_input_dict = doge_coin_transaction_input_instance.to_dict()
# create an instance of DogeCoinTransactionInput from a dict
doge_coin_transaction_input_form_dict = doge_coin_transaction_input.from_dict(doge_coin_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


