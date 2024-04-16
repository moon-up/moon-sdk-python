# BitcoinAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**BitcoinTransactionOutput**](BitcoinTransactionOutput.md) |  | [optional] 

## Example

```python
from openapi_client.models.bitcoin_api_response import BitcoinAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BitcoinAPIResponse from a JSON string
bitcoin_api_response_instance = BitcoinAPIResponse.from_json(json)
# print the JSON string representation of the object
print(BitcoinAPIResponse.to_json())

# convert the object into a dict
bitcoin_api_response_dict = bitcoin_api_response_instance.to_dict()
# create an instance of BitcoinAPIResponse from a dict
bitcoin_api_response_form_dict = bitcoin_api_response.from_dict(bitcoin_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


