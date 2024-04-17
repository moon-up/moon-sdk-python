# TransactionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moon_scan_url** | **str** |  | [optional] 
**transaction_hash** | **str** |  | 
**signed_transaction** | **str** |  | 
**signed_message** | **str** |  | [optional] 
**raw_transaction** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**transaction** | [**Tx**](Tx.md) |  | [optional] 
**user_ops** | [**List[TransactionRequest]**](TransactionRequest.md) |  | [optional] 
**userop_transaction** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.transaction_data import TransactionData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionData from a JSON string
transaction_data_instance = TransactionData.from_json(json)
# print the JSON string representation of the object
print(TransactionData.to_json())

# convert the object into a dict
transaction_data_dict = transaction_data_instance.to_dict()
# create an instance of TransactionData from a dict
transaction_data_form_dict = transaction_data.from_dict(transaction_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


