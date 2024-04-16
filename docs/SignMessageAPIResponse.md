# SignMessageAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**TransactionData**](TransactionData.md) |  | [optional] 

## Example

```python
from openapi_client.models.sign_message_api_response import SignMessageAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignMessageAPIResponse from a JSON string
sign_message_api_response_instance = SignMessageAPIResponse.from_json(json)
# print the JSON string representation of the object
print(SignMessageAPIResponse.to_json())

# convert the object into a dict
sign_message_api_response_dict = sign_message_api_response_instance.to_dict()
# create an instance of SignMessageAPIResponse from a dict
sign_message_api_response_form_dict = sign_message_api_response.from_dict(sign_message_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


