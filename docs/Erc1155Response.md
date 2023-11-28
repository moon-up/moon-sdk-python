# Erc1155Response


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
**balance_of** | **str** |  | [optional] 
**balance_of_batch** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.erc1155_response import Erc1155Response

# TODO update the JSON string below
json = "{}"
# create an instance of Erc1155Response from a JSON string
erc1155_response_instance = Erc1155Response.from_json(json)
# print the JSON string representation of the object
print Erc1155Response.to_json()

# convert the object into a dict
erc1155_response_dict = erc1155_response_instance.to_dict()
# create an instance of Erc1155Response from a dict
erc1155_response_form_dict = erc1155_response.from_dict(erc1155_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


