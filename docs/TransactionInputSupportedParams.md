# TransactionInputSupportedParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_data** | [**TransactionInputSupportedParamsPartnerData**](TransactionInputSupportedParamsPartnerData.md) |  | 
**theme** | [**TransactionInputSupportedParamsTheme**](TransactionInputSupportedParamsTheme.md) |  | 

## Example

```python
from moonsdk.models.transaction_input_supported_params import TransactionInputSupportedParams

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInputSupportedParams from a JSON string
transaction_input_supported_params_instance = TransactionInputSupportedParams.from_json(json)
# print the JSON string representation of the object
print(TransactionInputSupportedParams.to_json())

# convert the object into a dict
transaction_input_supported_params_dict = transaction_input_supported_params_instance.to_dict()
# create an instance of TransactionInputSupportedParams from a dict
transaction_input_supported_params_form_dict = transaction_input_supported_params.from_dict(transaction_input_supported_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


