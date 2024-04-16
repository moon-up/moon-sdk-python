# BitcoinCashTransactionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.bitcoin_cash_transaction_input import BitcoinCashTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of BitcoinCashTransactionInput from a JSON string
bitcoin_cash_transaction_input_instance = BitcoinCashTransactionInput.from_json(json)
# print the JSON string representation of the object
print(BitcoinCashTransactionInput.to_json())

# convert the object into a dict
bitcoin_cash_transaction_input_dict = bitcoin_cash_transaction_input_instance.to_dict()
# create an instance of BitcoinCashTransactionInput from a dict
bitcoin_cash_transaction_input_form_dict = bitcoin_cash_transaction_input.from_dict(bitcoin_cash_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


