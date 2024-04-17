# EosTransactionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_tx** | **str** |  | [optional] 
**transaction_hash** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.eos_transaction_output import EosTransactionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EosTransactionOutput from a JSON string
eos_transaction_output_instance = EosTransactionOutput.from_json(json)
# print the JSON string representation of the object
print(EosTransactionOutput.to_json())

# convert the object into a dict
eos_transaction_output_dict = eos_transaction_output_instance.to_dict()
# create an instance of EosTransactionOutput from a dict
eos_transaction_output_form_dict = eos_transaction_output.from_dict(eos_transaction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


