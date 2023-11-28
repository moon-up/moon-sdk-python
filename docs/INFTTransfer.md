# INFTTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** |  | 
**contract** | **str** |  | 
**log_index** | **str** |  | 
**token_contract_type** | **str** |  | 
**token_name** | **str** |  | 
**token_symbol** | **str** |  | 
**triggers** | [**List[TriggerOutput]**](TriggerOutput.md) |  | [optional] 
**operator** | **str** |  | 
**var_from** | **str** |  | 
**to** | **str** |  | 
**token_id** | **str** |  | 
**amount** | **str** |  | 

## Example

```python
from openapi_client.models.inft_transfer import INFTTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of INFTTransfer from a JSON string
inft_transfer_instance = INFTTransfer.from_json(json)
# print the JSON string representation of the object
print INFTTransfer.to_json()

# convert the object into a dict
inft_transfer_dict = inft_transfer_instance.to_dict()
# create an instance of INFTTransfer from a dict
inft_transfer_form_dict = inft_transfer.from_dict(inft_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


