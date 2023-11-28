# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TokenSwapParams(BaseModel):
    """
    TokenSwapParams
    """ # noqa: E501
    to: Optional[StrictStr] = None
    data: Optional[StrictStr] = None
    input: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    nonce: Optional[StrictStr] = None
    gas: Optional[StrictStr] = None
    gas_price: Optional[StrictStr] = Field(default=None, alias="gasPrice")
    chain_id: Optional[StrictStr] = None
    encoding: Optional[StrictStr] = None
    eoa: Optional[StrictBool] = Field(default=None, alias="EOA")
    contract_address: Optional[StrictStr] = None
    token_id: Optional[StrictStr] = None
    token_ids: Optional[StrictStr] = None
    approved: Optional[StrictBool] = None
    broadcast: Optional[StrictBool] = None
    token_in: StrictStr = Field(alias="tokenIn")
    token_out: StrictStr = Field(alias="tokenOut")
    token_in_decimals: Union[StrictFloat, StrictInt] = Field(alias="tokenInDecimals")
    token_out_decimals: Union[StrictFloat, StrictInt] = Field(alias="tokenOutDecimals")
    amount_in: StrictStr = Field(alias="amountIn")
    slippage: StrictStr
    recipient: StrictStr
    referrer: StrictStr
    __properties: ClassVar[List[str]] = ["to", "data", "input", "value", "nonce", "gas", "gasPrice", "chain_id", "encoding", "EOA", "contract_address", "token_id", "token_ids", "approved", "broadcast", "tokenIn", "tokenOut", "tokenInDecimals", "tokenOutDecimals", "amountIn", "slippage", "recipient", "referrer"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TokenSwapParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TokenSwapParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "to": obj.get("to"),
            "data": obj.get("data"),
            "input": obj.get("input"),
            "value": obj.get("value"),
            "nonce": obj.get("nonce"),
            "gas": obj.get("gas"),
            "gasPrice": obj.get("gasPrice"),
            "chain_id": obj.get("chain_id"),
            "encoding": obj.get("encoding"),
            "EOA": obj.get("EOA"),
            "contract_address": obj.get("contract_address"),
            "token_id": obj.get("token_id"),
            "token_ids": obj.get("token_ids"),
            "approved": obj.get("approved"),
            "broadcast": obj.get("broadcast"),
            "tokenIn": obj.get("tokenIn"),
            "tokenOut": obj.get("tokenOut"),
            "tokenInDecimals": obj.get("tokenInDecimals"),
            "tokenOutDecimals": obj.get("tokenOutDecimals"),
            "amountIn": obj.get("amountIn"),
            "slippage": obj.get("slippage"),
            "recipient": obj.get("recipient"),
            "referrer": obj.get("referrer")
        })
        return _obj


