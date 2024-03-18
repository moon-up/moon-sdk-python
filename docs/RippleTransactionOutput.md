# RippleTransactionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_tx** | **str** |  | [optional] 
**transaction_hash** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.ripple_transaction_output import RippleTransactionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RippleTransactionOutput from a JSON string
ripple_transaction_output_instance = RippleTransactionOutput.from_json(json)
# print the JSON string representation of the object
print RippleTransactionOutput.to_json()

# convert the object into a dict
ripple_transaction_output_dict = ripple_transaction_output_instance.to_dict()
# create an instance of RippleTransactionOutput from a dict
ripple_transaction_output_form_dict = ripple_transaction_output.from_dict(ripple_transaction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


