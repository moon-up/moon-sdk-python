# SupportedPaymentTypesCurrencyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**SupportedPaymentTypesMessage**](SupportedPaymentTypesMessage.md) |  | 

## Example

```python
from moonsdk.models.supported_payment_types_currency_response import SupportedPaymentTypesCurrencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedPaymentTypesCurrencyResponse from a JSON string
supported_payment_types_currency_response_instance = SupportedPaymentTypesCurrencyResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedPaymentTypesCurrencyResponse.to_json())

# convert the object into a dict
supported_payment_types_currency_response_dict = supported_payment_types_currency_response_instance.to_dict()
# create an instance of SupportedPaymentTypesCurrencyResponse from a dict
supported_payment_types_currency_response_form_dict = supported_payment_types_currency_response.from_dict(supported_payment_types_currency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


