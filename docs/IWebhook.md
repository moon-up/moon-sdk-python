# IWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**chain_id** | **str** |  | 
**logs** | [**List[Log]**](Log.md) |  | 
**txs** | [**List[Transaction]**](Transaction.md) |  | 
**txs_internal** | [**List[InternalTransaction]**](InternalTransaction.md) |  | 
**abi** | [**List[AbiItem]**](AbiItem.md) |  | 
**retries** | **float** |  | 
**confirmed** | **bool** |  | 
**tag** | **str** |  | 
**stream_id** | **str** |  | 
**erc20_transfers** | [**List[IERC20Transfer]**](IERC20Transfer.md) |  | 
**erc20_approvals** | [**List[IERC20Approval]**](IERC20Approval.md) |  | 
**nft_transfers** | [**List[INFTTransfer]**](INFTTransfer.md) |  | 
**native_balances** | [**List[INativeBalance]**](INativeBalance.md) |  | 
**nft_approvals** | [**IOldNFTApproval**](IOldNFTApproval.md) |  | 
**nft_token_approvals** | [**List[INFTApproval]**](INFTApproval.md) |  | 

## Example

```python
from moonsdk.models.i_webhook import IWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of IWebhook from a JSON string
i_webhook_instance = IWebhook.from_json(json)
# print the JSON string representation of the object
print IWebhook.to_json()

# convert the object into a dict
i_webhook_dict = i_webhook_instance.to_dict()
# create an instance of IWebhook from a dict
i_webhook_form_dict = i_webhook.from_dict(i_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


