# TransactionAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**transaction_hash** | **object** |  | [optional] 
**signed_tx** | **object** |  | [optional] 
**data** | [**Transaction**](Transaction.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_api_response import TransactionAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionAPIResponse from a JSON string
transaction_api_response_instance = TransactionAPIResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionAPIResponse.to_json())

# convert the object into a dict
transaction_api_response_dict = transaction_api_response_instance.to_dict()
# create an instance of TransactionAPIResponse from a dict
transaction_api_response_form_dict = transaction_api_response.from_dict(transaction_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


