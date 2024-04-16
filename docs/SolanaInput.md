# SolanaInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.solana_input import SolanaInput

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaInput from a JSON string
solana_input_instance = SolanaInput.from_json(json)
# print the JSON string representation of the object
print(SolanaInput.to_json())

# convert the object into a dict
solana_input_dict = solana_input_instance.to_dict()
# create an instance of SolanaInput from a dict
solana_input_form_dict = solana_input.from_dict(solana_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


