# LitecoinTransactionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_tx** | **str** |  | [optional] 
**transaction_hash** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.litecoin_transaction_output import LitecoinTransactionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of LitecoinTransactionOutput from a JSON string
litecoin_transaction_output_instance = LitecoinTransactionOutput.from_json(json)
# print the JSON string representation of the object
print(LitecoinTransactionOutput.to_json())

# convert the object into a dict
litecoin_transaction_output_dict = litecoin_transaction_output_instance.to_dict()
# create an instance of LitecoinTransactionOutput from a dict
litecoin_transaction_output_form_dict = litecoin_transaction_output.from_dict(litecoin_transaction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


