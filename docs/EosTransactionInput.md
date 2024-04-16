# EosTransactionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.eos_transaction_input import EosTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of EosTransactionInput from a JSON string
eos_transaction_input_instance = EosTransactionInput.from_json(json)
# print the JSON string representation of the object
print(EosTransactionInput.to_json())

# convert the object into a dict
eos_transaction_input_dict = eos_transaction_input_instance.to_dict()
# create an instance of EosTransactionInput from a dict
eos_transaction_input_form_dict = eos_transaction_input.from_dict(eos_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


