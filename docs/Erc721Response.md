# Erc721Response


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
**balance_of** | **str** |  | [optional] 
**owner_of** | **str** |  | [optional] 
**token_uri** | **str** |  | [optional] 
**contract_address** | **str** |  | [optional] 
**is_approved_for_all** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.erc721_response import Erc721Response

# TODO update the JSON string below
json = "{}"
# create an instance of Erc721Response from a JSON string
erc721_response_instance = Erc721Response.from_json(json)
# print the JSON string representation of the object
print Erc721Response.to_json()

# convert the object into a dict
erc721_response_dict = erc721_response_instance.to_dict()
# create an instance of Erc721Response from a dict
erc721_response_form_dict = erc721_response.from_dict(erc721_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


