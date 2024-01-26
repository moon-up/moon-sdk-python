# UniswapInput


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
**token_a** | **str** |  | [optional] 
**token_b** | **str** |  | [optional] 
**amount_a** | **str** |  | [optional] 
**amount_b** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.uniswap_input import UniswapInput

# TODO update the JSON string below
json = "{}"
# create an instance of UniswapInput from a JSON string
uniswap_input_instance = UniswapInput.from_json(json)
# print the JSON string representation of the object
print UniswapInput.to_json()

# convert the object into a dict
uniswap_input_dict = uniswap_input_instance.to_dict()
# create an instance of UniswapInput from a dict
uniswap_input_form_dict = uniswap_input.from_dict(uniswap_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


