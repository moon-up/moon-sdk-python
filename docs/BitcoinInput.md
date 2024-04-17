# BitcoinInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from moonsdk.models.bitcoin_input import BitcoinInput

# TODO update the JSON string below
json = "{}"
# create an instance of BitcoinInput from a JSON string
bitcoin_input_instance = BitcoinInput.from_json(json)
# print the JSON string representation of the object
print(BitcoinInput.to_json())

# convert the object into a dict
bitcoin_input_dict = bitcoin_input_instance.to_dict()
# create an instance of BitcoinInput from a dict
bitcoin_input_form_dict = bitcoin_input.from_dict(bitcoin_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


