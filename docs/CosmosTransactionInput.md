# CosmosTransactionInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.cosmos_transaction_input import CosmosTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of CosmosTransactionInput from a JSON string
cosmos_transaction_input_instance = CosmosTransactionInput.from_json(json)
# print the JSON string representation of the object
print CosmosTransactionInput.to_json()

# convert the object into a dict
cosmos_transaction_input_dict = cosmos_transaction_input_instance.to_dict()
# create an instance of CosmosTransactionInput from a dict
cosmos_transaction_input_form_dict = cosmos_transaction_input.from_dict(cosmos_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


