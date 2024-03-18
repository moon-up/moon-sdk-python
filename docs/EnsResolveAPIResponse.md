# EnsResolveAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**EnsResolveResponse**](EnsResolveResponse.md) |  | [optional] 

## Example

```python
from moonsdk.models.ens_resolve_api_response import EnsResolveAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnsResolveAPIResponse from a JSON string
ens_resolve_api_response_instance = EnsResolveAPIResponse.from_json(json)
# print the JSON string representation of the object
print EnsResolveAPIResponse.to_json()

# convert the object into a dict
ens_resolve_api_response_dict = ens_resolve_api_response_instance.to_dict()
# create an instance of EnsResolveAPIResponse from a dict
ens_resolve_api_response_form_dict = ens_resolve_api_response.from_dict(ens_resolve_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


