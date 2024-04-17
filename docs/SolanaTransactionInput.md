# SolanaTransactionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from moonsdk.models.solana_transaction_input import SolanaTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaTransactionInput from a JSON string
solana_transaction_input_instance = SolanaTransactionInput.from_json(json)
# print the JSON string representation of the object
print(SolanaTransactionInput.to_json())

# convert the object into a dict
solana_transaction_input_dict = solana_transaction_input_instance.to_dict()
# create an instance of SolanaTransactionInput from a dict
solana_transaction_input_form_dict = solana_transaction_input.from_dict(solana_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


