# CosmosTransactionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_tx** | **str** |  | [optional] 
**transaction_hash** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.cosmos_transaction_output import CosmosTransactionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CosmosTransactionOutput from a JSON string
cosmos_transaction_output_instance = CosmosTransactionOutput.from_json(json)
# print the JSON string representation of the object
print CosmosTransactionOutput.to_json()

# convert the object into a dict
cosmos_transaction_output_dict = cosmos_transaction_output_instance.to_dict()
# create an instance of CosmosTransactionOutput from a dict
cosmos_transaction_output_form_dict = cosmos_transaction_output.from_dict(cosmos_transaction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


