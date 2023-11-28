# RippleTransactionInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.ripple_transaction_input import RippleTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of RippleTransactionInput from a JSON string
ripple_transaction_input_instance = RippleTransactionInput.from_json(json)
# print the JSON string representation of the object
print RippleTransactionInput.to_json()

# convert the object into a dict
ripple_transaction_input_dict = ripple_transaction_input_instance.to_dict()
# create an instance of RippleTransactionInput from a dict
ripple_transaction_input_form_dict = ripple_transaction_input.from_dict(ripple_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


