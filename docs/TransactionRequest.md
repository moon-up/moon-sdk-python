# TransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**max_fee_per_gas** | **str** |  | [optional] 
**max_priority_fee_per_gas** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.transaction_request import TransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequest from a JSON string
transaction_request_instance = TransactionRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionRequest.to_json())

# convert the object into a dict
transaction_request_dict = transaction_request_instance.to_dict()
# create an instance of TransactionRequest from a dict
transaction_request_form_dict = transaction_request.from_dict(transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


