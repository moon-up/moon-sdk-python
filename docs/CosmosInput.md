# CosmosInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.cosmos_input import CosmosInput

# TODO update the JSON string below
json = "{}"
# create an instance of CosmosInput from a JSON string
cosmos_input_instance = CosmosInput.from_json(json)
# print the JSON string representation of the object
print CosmosInput.to_json()

# convert the object into a dict
cosmos_input_dict = cosmos_input_instance.to_dict()
# create an instance of CosmosInput from a dict
cosmos_input_form_dict = cosmos_input.from_dict(cosmos_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


