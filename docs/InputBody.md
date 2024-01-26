# InputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**input** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 
**gas** | **str** |  | [optional] 
**gas_price** | **str** |  | [optional] 
**chain_id** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**eoa** | **bool** |  | [optional] 
**contract_address** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_ids** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**broadcast** | **bool** |  | [optional] 

## Example

```python
from moonsdk.models.input_body import InputBody

# TODO update the JSON string below
json = "{}"
# create an instance of InputBody from a JSON string
input_body_instance = InputBody.from_json(json)
# print the JSON string representation of the object
print InputBody.to_json()

# convert the object into a dict
input_body_dict = input_body_instance.to_dict()
# create an instance of InputBody from a dict
input_body_form_dict = input_body.from_dict(input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


