# AccountControllerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccountControllerResponseData**](AccountControllerResponseData.md) |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.account_controller_response import AccountControllerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountControllerResponse from a JSON string
account_controller_response_instance = AccountControllerResponse.from_json(json)
# print the JSON string representation of the object
print AccountControllerResponse.to_json()

# convert the object into a dict
account_controller_response_dict = account_controller_response_instance.to_dict()
# create an instance of AccountControllerResponse from a dict
account_controller_response_form_dict = account_controller_response.from_dict(account_controller_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


