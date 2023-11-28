# CreateAccountInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_account_input import CreateAccountInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountInput from a JSON string
create_account_input_instance = CreateAccountInput.from_json(json)
# print the JSON string representation of the object
print CreateAccountInput.to_json()

# convert the object into a dict
create_account_input_dict = create_account_input_instance.to_dict()
# create an instance of CreateAccountInput from a dict
create_account_input_form_dict = create_account_input.from_dict(create_account_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


