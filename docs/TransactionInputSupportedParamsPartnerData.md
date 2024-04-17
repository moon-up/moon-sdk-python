# TransactionInputSupportedParamsPartnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_url** | [**TransactionInputSupportedParamsPartnerDataRedirectUrl**](TransactionInputSupportedParamsPartnerDataRedirectUrl.md) |  | 

## Example

```python
from moonsdk.models.transaction_input_supported_params_partner_data import TransactionInputSupportedParamsPartnerData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInputSupportedParamsPartnerData from a JSON string
transaction_input_supported_params_partner_data_instance = TransactionInputSupportedParamsPartnerData.from_json(json)
# print the JSON string representation of the object
print(TransactionInputSupportedParamsPartnerData.to_json())

# convert the object into a dict
transaction_input_supported_params_partner_data_dict = transaction_input_supported_params_partner_data_instance.to_dict()
# create an instance of TransactionInputSupportedParamsPartnerData from a dict
transaction_input_supported_params_partner_data_form_dict = transaction_input_supported_params_partner_data.from_dict(transaction_input_supported_params_partner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


