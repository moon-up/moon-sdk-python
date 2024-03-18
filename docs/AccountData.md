# AccountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.account_data import AccountData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountData from a JSON string
account_data_instance = AccountData.from_json(json)
# print the JSON string representation of the object
print AccountData.to_json()

# convert the object into a dict
account_data_dict = account_data_instance.to_dict()
# create an instance of AccountData from a dict
account_data_form_dict = account_data.from_dict(account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


