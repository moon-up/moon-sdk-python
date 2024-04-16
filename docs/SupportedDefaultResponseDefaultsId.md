# SupportedDefaultResponseDefaultsId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**payment_method** | **str** |  | 
**amount** | **float** |  | 
**target** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from openapi_client.models.supported_default_response_defaults_id import SupportedDefaultResponseDefaultsId

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedDefaultResponseDefaultsId from a JSON string
supported_default_response_defaults_id_instance = SupportedDefaultResponseDefaultsId.from_json(json)
# print the JSON string representation of the object
print(SupportedDefaultResponseDefaultsId.to_json())

# convert the object into a dict
supported_default_response_defaults_id_dict = supported_default_response_defaults_id_instance.to_dict()
# create an instance of SupportedDefaultResponseDefaultsId from a dict
supported_default_response_defaults_id_form_dict = supported_default_response_defaults_id.from_dict(supported_default_response_defaults_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


