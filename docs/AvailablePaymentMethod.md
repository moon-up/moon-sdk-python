# AvailablePaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** |  | 
**name** | **str** |  | 
**payment_type_id** | **str** |  | 

## Example

```python
from moonsdk.models.available_payment_method import AvailablePaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePaymentMethod from a JSON string
available_payment_method_instance = AvailablePaymentMethod.from_json(json)
# print the JSON string representation of the object
print(AvailablePaymentMethod.to_json())

# convert the object into a dict
available_payment_method_dict = available_payment_method_instance.to_dict()
# create an instance of AvailablePaymentMethod from a dict
available_payment_method_form_dict = available_payment_method.from_dict(available_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


