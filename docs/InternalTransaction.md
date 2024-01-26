# InternalTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **str** |  | 
**value** | **str** |  | 
**transaction_hash** | **str** |  | 
**gas** | **str** |  | 

## Example

```python
from moonsdk.models.internal_transaction import InternalTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransaction from a JSON string
internal_transaction_instance = InternalTransaction.from_json(json)
# print the JSON string representation of the object
print InternalTransaction.to_json()

# convert the object into a dict
internal_transaction_dict = internal_transaction_instance.to_dict()
# create an instance of InternalTransaction from a dict
internal_transaction_form_dict = internal_transaction.from_dict(internal_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


