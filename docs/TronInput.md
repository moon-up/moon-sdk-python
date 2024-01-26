# TronInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.tron_input import TronInput

# TODO update the JSON string below
json = "{}"
# create an instance of TronInput from a JSON string
tron_input_instance = TronInput.from_json(json)
# print the JSON string representation of the object
print TronInput.to_json()

# convert the object into a dict
tron_input_dict = tron_input_instance.to_dict()
# create an instance of TronInput from a dict
tron_input_form_dict = tron_input.from_dict(tron_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


