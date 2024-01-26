# TransactionInputMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** |  | 

## Example

```python
from moonsdk.models.transaction_input_meta_data import TransactionInputMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInputMetaData from a JSON string
transaction_input_meta_data_instance = TransactionInputMetaData.from_json(json)
# print the JSON string representation of the object
print TransactionInputMetaData.to_json()

# convert the object into a dict
transaction_input_meta_data_dict = transaction_input_meta_data_instance.to_dict()
# create an instance of TransactionInputMetaData from a dict
transaction_input_meta_data_form_dict = transaction_input_meta_data.from_dict(transaction_input_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


