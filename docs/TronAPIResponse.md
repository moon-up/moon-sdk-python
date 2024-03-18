# TronAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**TronTransactionOutput**](TronTransactionOutput.md) |  | [optional] 

## Example

```python
from moonsdk.models.tron_api_response import TronAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TronAPIResponse from a JSON string
tron_api_response_instance = TronAPIResponse.from_json(json)
# print the JSON string representation of the object
print TronAPIResponse.to_json()

# convert the object into a dict
tron_api_response_dict = tron_api_response_instance.to_dict()
# create an instance of TronAPIResponse from a dict
tron_api_response_form_dict = tron_api_response.from_dict(tron_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


