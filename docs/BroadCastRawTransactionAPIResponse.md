# BroadCastRawTransactionAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**BroadCastRawTransactionResponse**](BroadCastRawTransactionResponse.md) |  | [optional] 

## Example

```python
from moonsdk.models.broad_cast_raw_transaction_api_response import BroadCastRawTransactionAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BroadCastRawTransactionAPIResponse from a JSON string
broad_cast_raw_transaction_api_response_instance = BroadCastRawTransactionAPIResponse.from_json(json)
# print the JSON string representation of the object
print(BroadCastRawTransactionAPIResponse.to_json())

# convert the object into a dict
broad_cast_raw_transaction_api_response_dict = broad_cast_raw_transaction_api_response_instance.to_dict()
# create an instance of BroadCastRawTransactionAPIResponse from a dict
broad_cast_raw_transaction_api_response_form_dict = broad_cast_raw_transaction_api_response.from_dict(broad_cast_raw_transaction_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


