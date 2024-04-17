# DogeCoinAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**DogeCoinTransactionOutput**](DogeCoinTransactionOutput.md) |  | [optional] 

## Example

```python
from moonsdk.models.doge_coin_api_response import DogeCoinAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DogeCoinAPIResponse from a JSON string
doge_coin_api_response_instance = DogeCoinAPIResponse.from_json(json)
# print the JSON string representation of the object
print(DogeCoinAPIResponse.to_json())

# convert the object into a dict
doge_coin_api_response_dict = doge_coin_api_response_instance.to_dict()
# create an instance of DogeCoinAPIResponse from a dict
doge_coin_api_response_form_dict = doge_coin_api_response.from_dict(doge_coin_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


