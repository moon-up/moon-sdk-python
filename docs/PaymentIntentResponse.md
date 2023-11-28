# PaymentIntentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, str]** |  | [optional] 
**uri** | **str** |  | [optional] 
**qr_code** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**network** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | 

## Example

```python
from openapi_client.models.payment_intent_response import PaymentIntentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentResponse from a JSON string
payment_intent_response_instance = PaymentIntentResponse.from_json(json)
# print the JSON string representation of the object
print PaymentIntentResponse.to_json()

# convert the object into a dict
payment_intent_response_dict = payment_intent_response_instance.to_dict()
# create an instance of PaymentIntentResponse from a dict
payment_intent_response_form_dict = payment_intent_response.from_dict(payment_intent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


