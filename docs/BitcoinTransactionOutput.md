# BitcoinTransactionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_tx** | **str** |  | [optional] 
**transaction_hash** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.bitcoin_transaction_output import BitcoinTransactionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BitcoinTransactionOutput from a JSON string
bitcoin_transaction_output_instance = BitcoinTransactionOutput.from_json(json)
# print the JSON string representation of the object
print BitcoinTransactionOutput.to_json()

# convert the object into a dict
bitcoin_transaction_output_dict = bitcoin_transaction_output_instance.to_dict()
# create an instance of BitcoinTransactionOutput from a dict
bitcoin_transaction_output_form_dict = bitcoin_transaction_output.from_dict(bitcoin_transaction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


