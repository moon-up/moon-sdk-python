# INFTApprovalERC1155


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** |  | 
**contract** | **str** |  | 
**log_index** | **str** |  | 
**account** | **str** |  | 
**operator** | **str** |  | 
**approved** | **bool** |  | 
**token_contract_type** | **str** |  | 
**token_name** | **str** |  | 
**token_symbol** | **str** |  | 

## Example

```python
from moonsdk.models.inft_approval_erc1155 import INFTApprovalERC1155

# TODO update the JSON string below
json = "{}"
# create an instance of INFTApprovalERC1155 from a JSON string
inft_approval_erc1155_instance = INFTApprovalERC1155.from_json(json)
# print the JSON string representation of the object
print INFTApprovalERC1155.to_json()

# convert the object into a dict
inft_approval_erc1155_dict = inft_approval_erc1155_instance.to_dict()
# create an instance of INFTApprovalERC1155 from a dict
inft_approval_erc1155_form_dict = inft_approval_erc1155.from_dict(inft_approval_erc1155_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


