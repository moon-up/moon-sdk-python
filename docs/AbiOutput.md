# AbiOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**components** | [**List[AbiOutput]**](AbiOutput.md) |  | [optional] 
**internal_type** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.abi_output import AbiOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AbiOutput from a JSON string
abi_output_instance = AbiOutput.from_json(json)
# print the JSON string representation of the object
print AbiOutput.to_json()

# convert the object into a dict
abi_output_dict = abi_output_instance.to_dict()
# create an instance of AbiOutput from a dict
abi_output_form_dict = abi_output.from_dict(abi_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


