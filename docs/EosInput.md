# EosInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.eos_input import EosInput

# TODO update the JSON string below
json = "{}"
# create an instance of EosInput from a JSON string
eos_input_instance = EosInput.from_json(json)
# print the JSON string representation of the object
print(EosInput.to_json())

# convert the object into a dict
eos_input_dict = eos_input_instance.to_dict()
# create an instance of EosInput from a dict
eos_input_form_dict = eos_input.from_dict(eos_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


