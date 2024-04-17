# ConveyorFinanceControllerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**InputBody**](InputBody.md) |  | [optional] 
**convey** | [**TransactionResponse**](TransactionResponse.md) |  | [optional] 
**data** | [**TransactionData**](TransactionData.md) |  | [optional] 
**tx** | [**TransactionResponseTx**](TransactionResponseTx.md) |  | [optional] 
**signed** | [**Transaction**](Transaction.md) |  | [optional] 
**success** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from moonsdk.models.conveyor_finance_controller_response import ConveyorFinanceControllerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConveyorFinanceControllerResponse from a JSON string
conveyor_finance_controller_response_instance = ConveyorFinanceControllerResponse.from_json(json)
# print the JSON string representation of the object
print(ConveyorFinanceControllerResponse.to_json())

# convert the object into a dict
conveyor_finance_controller_response_dict = conveyor_finance_controller_response_instance.to_dict()
# create an instance of ConveyorFinanceControllerResponse from a dict
conveyor_finance_controller_response_form_dict = conveyor_finance_controller_response.from_dict(conveyor_finance_controller_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


