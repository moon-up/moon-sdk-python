# GetSwapDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** |  | 
**dst** | **str** |  | 
**amount** | **str** |  | 
**var_from** | **str** |  | 
**slippage** | **float** |  | 
**protocols** | **str** |  | [optional] 
**fee** | **str** |  | [optional] 
**disable_estimate** | **bool** |  | [optional] 
**permit** | **str** |  | [optional] 
**include_tokens_info** | **bool** |  | [optional] 
**include_protocols** | **bool** |  | [optional] 
**compatibility** | **bool** |  | [optional] 
**allow_partial_fill** | **bool** |  | [optional] 
**parts** | **str** |  | [optional] 
**main_route_parts** | **str** |  | [optional] 
**connector_tokens** | **str** |  | [optional] 
**complexity_level** | **str** |  | [optional] 
**gas_limit** | **str** |  | [optional] 
**gas_price** | **str** |  | [optional] 
**referrer** | **str** |  | [optional] 
**receiver** | **str** |  | [optional] 
**chain_id** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.get_swap_dto import GetSwapDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetSwapDto from a JSON string
get_swap_dto_instance = GetSwapDto.from_json(json)
# print the JSON string representation of the object
print GetSwapDto.to_json()

# convert the object into a dict
get_swap_dto_dict = get_swap_dto_instance.to_dict()
# create an instance of GetSwapDto from a dict
get_swap_dto_form_dict = get_swap_dto.from_dict(get_swap_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


