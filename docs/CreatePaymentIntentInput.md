# CreatePaymentIntentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | 
**network** | **str** |  | [optional] 
**amount** | **float** |  | 
**currency** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.create_payment_intent_input import CreatePaymentIntentInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentIntentInput from a JSON string
create_payment_intent_input_instance = CreatePaymentIntentInput.from_json(json)
# print the JSON string representation of the object
print CreatePaymentIntentInput.to_json()

# convert the object into a dict
create_payment_intent_input_dict = create_payment_intent_input_instance.to_dict()
# create an instance of CreatePaymentIntentInput from a dict
create_payment_intent_input_form_dict = create_payment_intent_input.from_dict(create_payment_intent_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


