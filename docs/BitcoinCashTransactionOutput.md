# BitcoinCashTransactionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_tx** | **str** |  | [optional] 
**transaction_hash** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bitcoin_cash_transaction_output import BitcoinCashTransactionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BitcoinCashTransactionOutput from a JSON string
bitcoin_cash_transaction_output_instance = BitcoinCashTransactionOutput.from_json(json)
# print the JSON string representation of the object
print(BitcoinCashTransactionOutput.to_json())

# convert the object into a dict
bitcoin_cash_transaction_output_dict = bitcoin_cash_transaction_output_instance.to_dict()
# create an instance of BitcoinCashTransactionOutput from a dict
bitcoin_cash_transaction_output_form_dict = bitcoin_cash_transaction_output.from_dict(bitcoin_cash_transaction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


