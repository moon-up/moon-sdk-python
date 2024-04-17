# LitecoinInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.litecoin_input import LitecoinInput

# TODO update the JSON string below
json = "{}"
# create an instance of LitecoinInput from a JSON string
litecoin_input_instance = LitecoinInput.from_json(json)
# print the JSON string representation of the object
print(LitecoinInput.to_json())

# convert the object into a dict
litecoin_input_dict = litecoin_input_instance.to_dict()
# create an instance of LitecoinInput from a dict
litecoin_input_form_dict = litecoin_input.from_dict(litecoin_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


