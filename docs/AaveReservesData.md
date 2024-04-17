# AaveReservesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_atoken_balance** | **str** |  | 
**current_borrow_balance** | **str** |  | 
**principal_borrow_balance** | **str** |  | 
**borrow_rate_mode** | **str** |  | 
**borrow_rate** | **str** |  | 
**liquidity_rate** | **str** |  | 
**origination_fee** | **str** |  | 
**variable_borrow_index** | **str** |  | 
**last_update_timestamp** | **str** |  | 
**usage_as_collateral_enabled** | **str** |  | 

## Example

```python
from moonsdk.models.aave_reserves_data import AaveReservesData

# TODO update the JSON string below
json = "{}"
# create an instance of AaveReservesData from a JSON string
aave_reserves_data_instance = AaveReservesData.from_json(json)
# print the JSON string representation of the object
print(AaveReservesData.to_json())

# convert the object into a dict
aave_reserves_data_dict = aave_reserves_data_instance.to_dict()
# create an instance of AaveReservesData from a dict
aave_reserves_data_form_dict = aave_reserves_data.from_dict(aave_reserves_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


