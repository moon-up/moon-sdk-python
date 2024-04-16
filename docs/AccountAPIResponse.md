# AccountAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**AccountResponse**](AccountResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_api_response import AccountAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAPIResponse from a JSON string
account_api_response_instance = AccountAPIResponse.from_json(json)
# print the JSON string representation of the object
print(AccountAPIResponse.to_json())

# convert the object into a dict
account_api_response_dict = account_api_response_instance.to_dict()
# create an instance of AccountAPIResponse from a dict
account_api_response_form_dict = account_api_response.from_dict(account_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


