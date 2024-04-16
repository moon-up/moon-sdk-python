# AaveInput


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
**lending_pool** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**atoken_to_redeeem** | **str** |  | [optional] 
**ref_code** | **str** |  | [optional] 
**interest_rate_mode** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aave_input import AaveInput

# TODO update the JSON string below
json = "{}"
# create an instance of AaveInput from a JSON string
aave_input_instance = AaveInput.from_json(json)
# print the JSON string representation of the object
print(AaveInput.to_json())

# convert the object into a dict
aave_input_dict = aave_input_instance.to_dict()
# create an instance of AaveInput from a dict
aave_input_form_dict = aave_input.from_dict(aave_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


