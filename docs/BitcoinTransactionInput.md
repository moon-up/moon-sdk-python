# BitcoinTransactionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from moonsdk.models.bitcoin_transaction_input import BitcoinTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of BitcoinTransactionInput from a JSON string
bitcoin_transaction_input_instance = BitcoinTransactionInput.from_json(json)
# print the JSON string representation of the object
print(BitcoinTransactionInput.to_json())

# convert the object into a dict
bitcoin_transaction_input_dict = bitcoin_transaction_input_instance.to_dict()
# create an instance of BitcoinTransactionInput from a dict
bitcoin_transaction_input_form_dict = bitcoin_transaction_input.from_dict(bitcoin_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


