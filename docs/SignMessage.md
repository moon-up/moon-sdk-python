# SignMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **str** |  | 
**encoding** | **str** |  | [optional] 
**header** | **bool** |  | [optional] 
**signtype** | **bool** |  | [optional] 

## Example

```python
from moonsdk.models.sign_message import SignMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SignMessage from a JSON string
sign_message_instance = SignMessage.from_json(json)
# print the JSON string representation of the object
print(SignMessage.to_json())

# convert the object into a dict
sign_message_dict = sign_message_instance.to_dict()
# create an instance of SignMessage from a dict
sign_message_form_dict = sign_message.from_dict(sign_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


