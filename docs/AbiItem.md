# AbiItem

The abi to parse the log object of the contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous** | **bool** |  | [optional] 
**constant** | **bool** |  | [optional] 
**inputs** | [**List[AbiInput]**](AbiInput.md) |  | [optional] 
**name** | **str** |  | [optional] 
**outputs** | [**List[AbiOutput]**](AbiOutput.md) |  | [optional] 
**payable** | **bool** |  | [optional] 
**state_mutability** | **str** |  | [optional] 
**type** | **str** |  | 
**gas** | **float** |  | [optional] 

## Example

```python
from moonsdk.models.abi_item import AbiItem

# TODO update the JSON string below
json = "{}"
# create an instance of AbiItem from a JSON string
abi_item_instance = AbiItem.from_json(json)
# print the JSON string representation of the object
print AbiItem.to_json()

# convert the object into a dict
abi_item_dict = abi_item_instance.to_dict()
# create an instance of AbiItem from a dict
abi_item_form_dict = abi_item.from_dict(abi_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


