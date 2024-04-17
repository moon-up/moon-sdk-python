# RippleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.ripple_input import RippleInput

# TODO update the JSON string below
json = "{}"
# create an instance of RippleInput from a JSON string
ripple_input_instance = RippleInput.from_json(json)
# print the JSON string representation of the object
print(RippleInput.to_json())

# convert the object into a dict
ripple_input_dict = ripple_input_instance.to_dict()
# create an instance of RippleInput from a dict
ripple_input_form_dict = ripple_input.from_dict(ripple_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


