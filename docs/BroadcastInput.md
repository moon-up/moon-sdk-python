# BroadcastInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** |  | 
**raw_transaction** | **str** |  | 

## Example

```python
from moonsdk.models.broadcast_input import BroadcastInput

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastInput from a JSON string
broadcast_input_instance = BroadcastInput.from_json(json)
# print the JSON string representation of the object
print(BroadcastInput.to_json())

# convert the object into a dict
broadcast_input_dict = broadcast_input_instance.to_dict()
# create an instance of BroadcastInput from a dict
broadcast_input_form_dict = broadcast_input.from_dict(broadcast_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


