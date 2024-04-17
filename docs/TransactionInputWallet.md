# TransactionInputWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 

## Example

```python
from moonsdk.models.transaction_input_wallet import TransactionInputWallet

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInputWallet from a JSON string
transaction_input_wallet_instance = TransactionInputWallet.from_json(json)
# print the JSON string representation of the object
print(TransactionInputWallet.to_json())

# convert the object into a dict
transaction_input_wallet_dict = transaction_input_wallet_instance.to_dict()
# create an instance of TransactionInputWallet from a dict
transaction_input_wallet_form_dict = transaction_input_wallet.from_dict(transaction_input_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


