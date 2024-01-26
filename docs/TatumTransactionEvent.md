# TatumTransactionEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**test** | **bool** |  | 
**counter_address** | **str** |  | 
**address** | **str** |  | 
**mempool** | **bool** |  | 
**subscription_type** | **str** |  | 
**block_number** | **float** |  | 
**tx_id** | **str** |  | 
**chain** | **str** |  | 
**currency** | **str** |  | 

## Example

```python
from moonsdk.models.tatum_transaction_event import TatumTransactionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TatumTransactionEvent from a JSON string
tatum_transaction_event_instance = TatumTransactionEvent.from_json(json)
# print the JSON string representation of the object
print TatumTransactionEvent.to_json()

# convert the object into a dict
tatum_transaction_event_dict = tatum_transaction_event_instance.to_dict()
# create an instance of TatumTransactionEvent from a dict
tatum_transaction_event_form_dict = tatum_transaction_event.from_dict(tatum_transaction_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


