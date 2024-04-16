# Erc721Request


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
from openapi_client.models.erc721_request import Erc721Request

# TODO update the JSON string below
json = "{}"
# create an instance of Erc721Request from a JSON string
erc721_request_instance = Erc721Request.from_json(json)
# print the JSON string representation of the object
print(Erc721Request.to_json())

# convert the object into a dict
erc721_request_dict = erc721_request_instance.to_dict()
# create an instance of Erc721Request from a dict
erc721_request_form_dict = erc721_request.from_dict(erc721_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


