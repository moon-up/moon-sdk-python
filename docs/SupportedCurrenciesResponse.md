# SupportedCurrenciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**Message**](Message.md) |  | 

## Example

```python
from openapi_client.models.supported_currencies_response import SupportedCurrenciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedCurrenciesResponse from a JSON string
supported_currencies_response_instance = SupportedCurrenciesResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedCurrenciesResponse.to_json())

# convert the object into a dict
supported_currencies_response_dict = supported_currencies_response_instance.to_dict()
# create an instance of SupportedCurrenciesResponse from a dict
supported_currencies_response_form_dict = supported_currencies_response.from_dict(supported_currencies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


