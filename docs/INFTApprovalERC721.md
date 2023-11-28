# INFTApprovalERC721


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** |  | 
**contract** | **str** |  | 
**log_index** | **str** |  | 
**owner** | **str** |  | 
**approved** | **str** |  | 
**token_id** | **str** |  | 
**token_contract_type** | **str** |  | 
**token_name** | **str** |  | 
**token_symbol** | **str** |  | 

## Example

```python
from openapi_client.models.inft_approval_erc721 import INFTApprovalERC721

# TODO update the JSON string below
json = "{}"
# create an instance of INFTApprovalERC721 from a JSON string
inft_approval_erc721_instance = INFTApprovalERC721.from_json(json)
# print the JSON string representation of the object
print INFTApprovalERC721.to_json()

# convert the object into a dict
inft_approval_erc721_dict = inft_approval_erc721_instance.to_dict()
# create an instance of INFTApprovalERC721 from a dict
inft_approval_erc721_form_dict = inft_approval_erc721.from_dict(inft_approval_erc721_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


