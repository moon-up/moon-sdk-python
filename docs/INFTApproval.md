# INFTApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** |  | 
**contract** | **str** |  | 
**log_index** | **str** |  | 
**token_contract_type** | **str** |  | 
**token_name** | **str** |  | 
**token_symbol** | **str** |  | 
**account** | **str** |  | 
**operator** | **str** |  | 
**approved_all** | **bool** |  | 
**token_id** | **str** |  | 

## Example

```python
from moonsdk.models.inft_approval import INFTApproval

# TODO update the JSON string below
json = "{}"
# create an instance of INFTApproval from a JSON string
inft_approval_instance = INFTApproval.from_json(json)
# print the JSON string representation of the object
print INFTApproval.to_json()

# convert the object into a dict
inft_approval_dict = inft_approval_instance.to_dict()
# create an instance of INFTApproval from a dict
inft_approval_form_dict = inft_approval.from_dict(inft_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


