# EnsResolveInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**chain_id** | **str** |  | 

## Example

```python
from moonsdk.models.ens_resolve_input import EnsResolveInput

# TODO update the JSON string below
json = "{}"
# create an instance of EnsResolveInput from a JSON string
ens_resolve_input_instance = EnsResolveInput.from_json(json)
# print the JSON string representation of the object
print(EnsResolveInput.to_json())

# convert the object into a dict
ens_resolve_input_dict = ens_resolve_input_instance.to_dict()
# create an instance of EnsResolveInput from a dict
ens_resolve_input_form_dict = ens_resolve_input.from_dict(ens_resolve_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


