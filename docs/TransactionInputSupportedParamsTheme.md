# TransactionInputSupportedParamsTheme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**border_radius** | **float** |  | 
**card_color** | **str** |  | 
**secondary_text_color** | **str** |  | 
**primary_text_color** | **str** |  | 
**secondary_color** | **str** |  | 
**primary_color** | **str** |  | 
**theme_name** | **str** |  | 
**is_dark** | **bool** |  | 

## Example

```python
from moonsdk.models.transaction_input_supported_params_theme import TransactionInputSupportedParamsTheme

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInputSupportedParamsTheme from a JSON string
transaction_input_supported_params_theme_instance = TransactionInputSupportedParamsTheme.from_json(json)
# print the JSON string representation of the object
print TransactionInputSupportedParamsTheme.to_json()

# convert the object into a dict
transaction_input_supported_params_theme_dict = transaction_input_supported_params_theme_instance.to_dict()
# create an instance of TransactionInputSupportedParamsTheme from a dict
transaction_input_supported_params_theme_form_dict = transaction_input_supported_params_theme.from_dict(transaction_input_supported_params_theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


