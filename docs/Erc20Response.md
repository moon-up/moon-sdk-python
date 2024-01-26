# Erc20Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **float** |  | [optional] 
**chain_id** | **float** |  | [optional] 
**data** | **str** |  | [optional] 
**gas** | **str** |  | [optional] 
**gas_price** | **str** |  | [optional] 
**gas_tip_cap** | **str** |  | [optional] 
**gas_fee_cap** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**nonce** | **float** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**blob_gas** | **str** |  | [optional] 
**blob_gas_fee_cap** | **str** |  | [optional] 
**blob_hashes** | **List[str]** |  | [optional] 
**v** | **str** |  | [optional] 
**r** | **str** |  | [optional] 
**s** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**decimals** | **str** |  | [optional] 
**total_supply** | **str** |  | [optional] 
**contract_address** | **str** |  | [optional] 
**balance_of** | **str** |  | [optional] 
**allowance** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.erc20_response import Erc20Response

# TODO update the JSON string below
json = "{}"
# create an instance of Erc20Response from a JSON string
erc20_response_instance = Erc20Response.from_json(json)
# print the JSON string representation of the object
print Erc20Response.to_json()

# convert the object into a dict
erc20_response_dict = erc20_response_instance.to_dict()
# create an instance of Erc20Response from a dict
erc20_response_form_dict = erc20_response.from_dict(erc20_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


