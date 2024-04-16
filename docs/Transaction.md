# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** |  | [optional] 
**signed_transaction** | **str** |  | [optional] 
**raw_transaction** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**transactions** | [**List[TransactionData]**](TransactionData.md) |  | [optional] 
**moon_scan_url** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**transaction** | [**Tx**](Tx.md) |  | [optional] 
**user_ops** | [**List[TransactionRequest]**](TransactionRequest.md) |  | [optional] 
**userop_transaction** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_form_dict = transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


