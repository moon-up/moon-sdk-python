# GetSupportedOnRampsResponseMessageInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | 
**icons** | [**GetSupportedOnRampsResponseMessageInnerIcons**](GetSupportedOnRampsResponseMessageInnerIcons.md) |  | 
**icon** | **str** |  | 

## Example

```python
from openapi_client.models.get_supported_on_ramps_response_message_inner import GetSupportedOnRampsResponseMessageInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupportedOnRampsResponseMessageInner from a JSON string
get_supported_on_ramps_response_message_inner_instance = GetSupportedOnRampsResponseMessageInner.from_json(json)
# print the JSON string representation of the object
print GetSupportedOnRampsResponseMessageInner.to_json()

# convert the object into a dict
get_supported_on_ramps_response_message_inner_dict = get_supported_on_ramps_response_message_inner_instance.to_dict()
# create an instance of GetSupportedOnRampsResponseMessageInner from a dict
get_supported_on_ramps_response_message_inner_form_dict = get_supported_on_ramps_response_message_inner.from_dict(get_supported_on_ramps_response_message_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


