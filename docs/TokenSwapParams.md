# TokenSwapParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**input** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 
**gas** | **str** |  | [optional] 
**gas_price** | **str** |  | [optional] 
**chain_id** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**eoa** | **bool** |  | [optional] 
**contract_address** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_ids** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**broadcast** | **bool** |  | [optional] 
**token_in** | **str** |  | 
**token_out** | **str** |  | 
**token_in_decimals** | **float** |  | 
**token_out_decimals** | **float** |  | 
**amount_in** | **str** |  | 
**slippage** | **str** |  | 
**recipient** | **str** |  | 
**referrer** | **str** |  | 

## Example

```python
from openapi_client.models.token_swap_params import TokenSwapParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenSwapParams from a JSON string
token_swap_params_instance = TokenSwapParams.from_json(json)
# print the JSON string representation of the object
print TokenSwapParams.to_json()

# convert the object into a dict
token_swap_params_dict = token_swap_params_instance.to_dict()
# create an instance of TokenSwapParams from a dict
token_swap_params_form_dict = token_swap_params.from_dict(token_swap_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


