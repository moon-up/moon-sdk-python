# NonceAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**NonceResponse**](NonceResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.nonce_api_response import NonceAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NonceAPIResponse from a JSON string
nonce_api_response_instance = NonceAPIResponse.from_json(json)
# print the JSON string representation of the object
print(NonceAPIResponse.to_json())

# convert the object into a dict
nonce_api_response_dict = nonce_api_response_instance.to_dict()
# create an instance of NonceAPIResponse from a dict
nonce_api_response_form_dict = nonce_api_response.from_dict(nonce_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


