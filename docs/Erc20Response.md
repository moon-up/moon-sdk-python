# Erc20Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moon_scan_url** | **str** |  | [optional] 
**transaction_hash** | **str** |  | 
**signed_transaction** | **str** |  | 
**signed_message** | **str** |  | [optional] 
**raw_transaction** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**transaction** | [**Dict[str, Tx]**](Tx.md) |  | [optional] 
**user_ops** | [**List[TransactionRequest]**](TransactionRequest.md) |  | [optional] 
**userop_transaction** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**decimals** | **str** |  | [optional] 
**total_supply** | **str** |  | [optional] 
**contract_address** | **str** |  | [optional] 
**balance_of** | **str** |  | [optional] 
**allowance** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.erc20_response import Erc20Response

# TODO update the JSON string below
json = "{}"
# create an instance of Erc20Response from a JSON string
erc20_response_instance = Erc20Response.from_json(json)
# print the JSON string representation of the object
print Erc20Response.to_json()

# convert the object into a dict
erc20_response_dict = erc20_response_instance.to_dict()
# create an instance of Erc20Response from a dict
erc20_response_form_dict = erc20_response.from_dict(erc20_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


