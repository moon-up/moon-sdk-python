# SupportedAssetResponseAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto** | **List[str]** |  | 
**payment_methods** | **List[str]** |  | 
**fiat** | **str** |  | 

## Example

```python
from moonsdk.models.supported_asset_response_assets_inner import SupportedAssetResponseAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedAssetResponseAssetsInner from a JSON string
supported_asset_response_assets_inner_instance = SupportedAssetResponseAssetsInner.from_json(json)
# print the JSON string representation of the object
print(SupportedAssetResponseAssetsInner.to_json())

# convert the object into a dict
supported_asset_response_assets_inner_dict = supported_asset_response_assets_inner_instance.to_dict()
# create an instance of SupportedAssetResponseAssetsInner from a dict
supported_asset_response_assets_inner_form_dict = supported_asset_response_assets_inner.from_dict(supported_asset_response_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


