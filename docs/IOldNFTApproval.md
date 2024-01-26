# IOldNFTApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**erc721** | [**List[INFTApprovalERC721]**](INFTApprovalERC721.md) |  | 
**erc1155** | [**List[INFTApprovalERC1155]**](INFTApprovalERC1155.md) |  | 

## Example

```python
from moonsdk.models.i_old_nft_approval import IOldNFTApproval

# TODO update the JSON string below
json = "{}"
# create an instance of IOldNFTApproval from a JSON string
i_old_nft_approval_instance = IOldNFTApproval.from_json(json)
# print the JSON string representation of the object
print IOldNFTApproval.to_json()

# convert the object into a dict
i_old_nft_approval_dict = i_old_nft_approval_instance.to_dict()
# create an instance of IOldNFTApproval from a dict
i_old_nft_approval_form_dict = i_old_nft_approval.from_dict(i_old_nft_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


