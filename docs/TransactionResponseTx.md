# TransactionResponseTx


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | 
**value** | **str** |  | 
**nonce** | **float** |  | 
**gas** | **str** |  | 
**to** | **str** |  | 
**var_from** | **str** |  | 

## Example

```python
from moonsdk.models.transaction_response_tx import TransactionResponseTx

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponseTx from a JSON string
transaction_response_tx_instance = TransactionResponseTx.from_json(json)
# print the JSON string representation of the object
print(TransactionResponseTx.to_json())

# convert the object into a dict
transaction_response_tx_dict = transaction_response_tx_instance.to_dict()
# create an instance of TransactionResponseTx from a dict
transaction_response_tx_form_dict = transaction_response_tx.from_dict(transaction_response_tx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


