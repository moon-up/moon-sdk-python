# TronTransactionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_tx** | **str** |  | [optional] 
**transaction_hash** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.tron_transaction_output import TronTransactionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TronTransactionOutput from a JSON string
tron_transaction_output_instance = TronTransactionOutput.from_json(json)
# print the JSON string representation of the object
print TronTransactionOutput.to_json()

# convert the object into a dict
tron_transaction_output_dict = tron_transaction_output_instance.to_dict()
# create an instance of TronTransactionOutput from a dict
tron_transaction_output_form_dict = tron_transaction_output.from_dict(tron_transaction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


