# SupportedDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaults** | [**SupportedDefaultResponseDefaults**](SupportedDefaultResponseDefaults.md) |  | 
**recommended** | [**SupportedDefaultResponseDefaultsId**](SupportedDefaultResponseDefaultsId.md) |  | 

## Example

```python
from moonsdk.models.supported_default_response import SupportedDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedDefaultResponse from a JSON string
supported_default_response_instance = SupportedDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedDefaultResponse.to_json())

# convert the object into a dict
supported_default_response_dict = supported_default_response_instance.to_dict()
# create an instance of SupportedDefaultResponse from a dict
supported_default_response_form_dict = supported_default_response.from_dict(supported_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


