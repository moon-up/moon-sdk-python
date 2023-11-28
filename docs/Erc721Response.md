# Erc721Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moon_scan_url** | **str** |  | [optional] 
**transaction_hash** | **str** |  | 
**signed_transaction** | **str** |  | 
**signed_message** | **str** |  | [optional] 
**raw_transaction** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**transaction** | [**Dict[str, Tx]**](Tx.md) |  | [optional] 
**user_ops** | [**List[TransactionRequest]**](TransactionRequest.md) |  | [optional] 
**userop_transaction** | **str** |  | [optional] 
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


