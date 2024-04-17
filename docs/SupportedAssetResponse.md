# SupportedAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**assets** | [**List[SupportedAssetResponseAssetsInner]**](SupportedAssetResponseAssetsInner.md) |  | 

## Example

```python
from moonsdk.models.supported_asset_response import SupportedAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedAssetResponse from a JSON string
supported_asset_response_instance = SupportedAssetResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedAssetResponse.to_json())

# convert the object into a dict
supported_asset_response_dict = supported_asset_response_instance.to_dict()
# create an instance of SupportedAssetResponse from a dict
supported_asset_response_form_dict = supported_asset_response.from_dict(supported_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


