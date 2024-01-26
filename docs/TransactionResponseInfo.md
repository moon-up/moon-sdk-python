# TransactionResponseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conveyor_gas** | **str** |  | 
**affiliate_gas** | **str** |  | 
**affiliate_aggregator** | **str** |  | 
**amount_out** | **str** |  | 
**amount_out_min** | **str** |  | 

## Example

```python
from moonsdk.models.transaction_response_info import TransactionResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponseInfo from a JSON string
transaction_response_info_instance = TransactionResponseInfo.from_json(json)
# print the JSON string representation of the object
print TransactionResponseInfo.to_json()

# convert the object into a dict
transaction_response_info_dict = transaction_response_info_instance.to_dict()
# create an instance of TransactionResponseInfo from a dict
transaction_response_info_form_dict = transaction_response_info.from_dict(transaction_response_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


