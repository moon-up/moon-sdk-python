# TronTransactionInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tron_transaction_input import TronTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of TronTransactionInput from a JSON string
tron_transaction_input_instance = TronTransactionInput.from_json(json)
# print the JSON string representation of the object
print TronTransactionInput.to_json()

# convert the object into a dict
tron_transaction_input_dict = tron_transaction_input_instance.to_dict()
# create an instance of TronTransactionInput from a dict
tron_transaction_input_form_dict = tron_transaction_input.from_dict(tron_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


