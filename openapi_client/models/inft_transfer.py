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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from openapi_client.models.trigger_output import TriggerOutput
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class INFTTransfer(BaseModel):
    """
    INFTTransfer
    """ # noqa: E501
    transaction_hash: StrictStr = Field(alias="transactionHash")
    contract: StrictStr
    log_index: StrictStr = Field(alias="logIndex")
    token_contract_type: StrictStr = Field(alias="tokenContractType")
    token_name: StrictStr = Field(alias="tokenName")
    token_symbol: StrictStr = Field(alias="tokenSymbol")
    triggers: Optional[List[TriggerOutput]] = None
    operator: Optional[StrictStr]
    var_from: StrictStr = Field(alias="from")
    to: StrictStr
    token_id: StrictStr = Field(alias="tokenId")
    amount: StrictStr
    __properties: ClassVar[List[str]] = ["transactionHash", "contract", "logIndex", "tokenContractType", "tokenName", "tokenSymbol", "triggers", "operator", "from", "to", "tokenId", "amount"]

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
        """Create an instance of INFTTransfer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in triggers (list)
        _items = []
        if self.triggers:
            for _item in self.triggers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['triggers'] = _items
        # set to None if operator (nullable) is None
        # and model_fields_set contains the field
        if self.operator is None and "operator" in self.model_fields_set:
            _dict['operator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of INFTTransfer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactionHash": obj.get("transactionHash"),
            "contract": obj.get("contract"),
            "logIndex": obj.get("logIndex"),
            "tokenContractType": obj.get("tokenContractType"),
            "tokenName": obj.get("tokenName"),
            "tokenSymbol": obj.get("tokenSymbol"),
            "triggers": [TriggerOutput.from_dict(_item) for _item in obj.get("triggers")] if obj.get("triggers") is not None else None,
            "operator": obj.get("operator"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "tokenId": obj.get("tokenId"),
            "amount": obj.get("amount")
        })
        return _obj


