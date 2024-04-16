# LitecoinAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**LitecoinTransactionOutput**](LitecoinTransactionOutput.md) |  | [optional] 

## Example

```python
from openapi_client.models.litecoin_api_response import LitecoinAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LitecoinAPIResponse from a JSON string
litecoin_api_response_instance = LitecoinAPIResponse.from_json(json)
# print the JSON string representation of the object
print(LitecoinAPIResponse.to_json())

# convert the object into a dict
litecoin_api_response_dict = litecoin_api_response_instance.to_dict()
# create an instance of LitecoinAPIResponse from a dict
litecoin_api_response_form_dict = litecoin_api_response.from_dict(litecoin_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


