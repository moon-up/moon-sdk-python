# SupportedPaymentTypesMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**googlepay** | [**PaymentType**](PaymentType.md) |  | 
**applepay** | [**PaymentType**](PaymentType.md) |  | 
**creditcard** | [**PaymentType**](PaymentType.md) |  | 

## Example

```python
from openapi_client.models.supported_payment_types_message import SupportedPaymentTypesMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedPaymentTypesMessage from a JSON string
supported_payment_types_message_instance = SupportedPaymentTypesMessage.from_json(json)
# print the JSON string representation of the object
print(SupportedPaymentTypesMessage.to_json())

# convert the object into a dict
supported_payment_types_message_dict = supported_payment_types_message_instance.to_dict()
# create an instance of SupportedPaymentTypesMessage from a dict
supported_payment_types_message_form_dict = supported_payment_types_message.from_dict(supported_payment_types_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


