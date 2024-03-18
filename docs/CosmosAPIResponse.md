# CosmosAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**CosmosTransactionOutput**](CosmosTransactionOutput.md) |  | [optional] 

## Example

```python
from moonsdk.models.cosmos_api_response import CosmosAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CosmosAPIResponse from a JSON string
cosmos_api_response_instance = CosmosAPIResponse.from_json(json)
# print the JSON string representation of the object
print CosmosAPIResponse.to_json()

# convert the object into a dict
cosmos_api_response_dict = cosmos_api_response_instance.to_dict()
# create an instance of CosmosAPIResponse from a dict
cosmos_api_response_form_dict = cosmos_api_response.from_dict(cosmos_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


