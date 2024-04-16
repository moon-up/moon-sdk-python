# LitecoinTransactionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**compress** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.litecoin_transaction_input import LitecoinTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of LitecoinTransactionInput from a JSON string
litecoin_transaction_input_instance = LitecoinTransactionInput.from_json(json)
# print the JSON string representation of the object
print(LitecoinTransactionInput.to_json())

# convert the object into a dict
litecoin_transaction_input_dict = litecoin_transaction_input_instance.to_dict()
# create an instance of LitecoinTransactionInput from a dict
litecoin_transaction_input_form_dict = litecoin_transaction_input.from_dict(litecoin_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


