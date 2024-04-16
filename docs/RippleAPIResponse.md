# RippleAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**RippleTransactionOutput**](RippleTransactionOutput.md) |  | [optional] 

## Example

```python
from openapi_client.models.ripple_api_response import RippleAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RippleAPIResponse from a JSON string
ripple_api_response_instance = RippleAPIResponse.from_json(json)
# print the JSON string representation of the object
print(RippleAPIResponse.to_json())

# convert the object into a dict
ripple_api_response_dict = ripple_api_response_instance.to_dict()
# create an instance of RippleAPIResponse from a dict
ripple_api_response_form_dict = ripple_api_response.from_dict(ripple_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


