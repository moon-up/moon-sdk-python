# Erc1155Request


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

## Example

```python
from openapi_client.models.erc1155_request import Erc1155Request

# TODO update the JSON string below
json = "{}"
# create an instance of Erc1155Request from a JSON string
erc1155_request_instance = Erc1155Request.from_json(json)
# print the JSON string representation of the object
print Erc1155Request.to_json()

# convert the object into a dict
erc1155_request_dict = erc1155_request_instance.to_dict()
# create an instance of Erc1155Request from a dict
erc1155_request_form_dict = erc1155_request.from_dict(erc1155_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


