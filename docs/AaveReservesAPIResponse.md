# AaveReservesAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**body** | [**InputBody**](InputBody.md) |  | [optional] 
**address** | **str** |  | [optional] 
**data** | [**AaveReservesData**](AaveReservesData.md) |  | [optional] 

## Example

```python
from openapi_client.models.aave_reserves_api_response import AaveReservesAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AaveReservesAPIResponse from a JSON string
aave_reserves_api_response_instance = AaveReservesAPIResponse.from_json(json)
# print the JSON string representation of the object
print(AaveReservesAPIResponse.to_json())

# convert the object into a dict
aave_reserves_api_response_dict = aave_reserves_api_response_instance.to_dict()
# create an instance of AaveReservesAPIResponse from a dict
aave_reserves_api_response_form_dict = aave_reserves_api_response.from_dict(aave_reserves_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


