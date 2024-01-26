# BroadCastRawTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | **str** |  | 

## Example

```python
from moonsdk.models.broad_cast_raw_transaction_response import BroadCastRawTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BroadCastRawTransactionResponse from a JSON string
broad_cast_raw_transaction_response_instance = BroadCastRawTransactionResponse.from_json(json)
# print the JSON string representation of the object
print BroadCastRawTransactionResponse.to_json()

# convert the object into a dict
broad_cast_raw_transaction_response_dict = broad_cast_raw_transaction_response_instance.to_dict()
# create an instance of BroadCastRawTransactionResponse from a dict
broad_cast_raw_transaction_response_form_dict = broad_cast_raw_transaction_response.from_dict(broad_cast_raw_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


