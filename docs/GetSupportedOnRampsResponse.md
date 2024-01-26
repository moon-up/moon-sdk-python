# GetSupportedOnRampsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**List[GetSupportedOnRampsResponseMessageInner]**](GetSupportedOnRampsResponseMessageInner.md) |  | 

## Example

```python
from moonsdk.models.get_supported_on_ramps_response import GetSupportedOnRampsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupportedOnRampsResponse from a JSON string
get_supported_on_ramps_response_instance = GetSupportedOnRampsResponse.from_json(json)
# print the JSON string representation of the object
print GetSupportedOnRampsResponse.to_json()

# convert the object into a dict
get_supported_on_ramps_response_dict = get_supported_on_ramps_response_instance.to_dict()
# create an instance of GetSupportedOnRampsResponse from a dict
get_supported_on_ramps_response_form_dict = get_supported_on_ramps_response.from_dict(get_supported_on_ramps_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


