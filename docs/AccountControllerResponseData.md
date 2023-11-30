# AccountControllerResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **float** |  | 
**balance** | **str** |  | 
**transaction_hash** | **str** |  | [optional] 
**signed_transaction** | **str** |  | [optional] 
**raw_transaction** | **str** |  | [optional] 
**data** | **str** |  | 
**transactions** | [**List[TransactionData]**](TransactionData.md) |  | [optional] 
**moon_scan_url** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**transaction** | [**Tx**](Tx.md) |  | [optional] 
**user_ops** | [**List[TransactionRequest]**](TransactionRequest.md) |  | [optional] 
**userop_transaction** | **str** |  | [optional] 
**keys** | **List[str]** |  | [optional] 
**address** | **str** |  | 
**name** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**header** | **bool** |  | [optional] 
**signtype** | **bool** |  | [optional] 
**domain** | **str** |  | 
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
**type** | **float** |  | [optional] 
**chain_id** | **float** |  | [optional] 
**gas** | **str** |  | [optional] 
**gas_price** | **str** |  | [optional] 
**gas_tip_cap** | **str** |  | [optional] 
**gas_fee_cap** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**blob_gas** | **str** |  | [optional] 
**blob_gas_fee_cap** | **str** |  | [optional] 
**blob_hashes** | **List[str]** |  | [optional] 
**v** | **str** |  | [optional] 
**r** | **str** |  | [optional] 
**s** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**decimals** | **str** |  | [optional] 
**total_supply** | **str** |  | [optional] 
**contract_address** | **str** |  | [optional] 
**balance_of** | **str** |  | [optional] 
**allowance** | **str** |  | [optional] 
**balance_of** | **str** |  | [optional] 
**balance_of_batch** | **str** |  | [optional] 
**success** | **bool** |  | 
**message** | **str** |  | 
**signed_tx** | **str** |  | [optional] 
**owner_of** | **str** |  | [optional] 
**token_uri** | **str** |  | [optional] 
**is_approved_for_all** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_controller_response_data import AccountControllerResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountControllerResponseData from a JSON string
account_controller_response_data_instance = AccountControllerResponseData.from_json(json)
# print the JSON string representation of the object
print AccountControllerResponseData.to_json()

# convert the object into a dict
account_controller_response_data_dict = account_controller_response_data_instance.to_dict()
# create an instance of AccountControllerResponseData from a dict
account_controller_response_data_form_dict = account_controller_response_data.from_dict(account_controller_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


