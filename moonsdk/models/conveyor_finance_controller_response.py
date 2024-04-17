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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from moonsdk.models.input_body import InputBody
from moonsdk.models.transaction import Transaction
from moonsdk.models.transaction_data import TransactionData
from moonsdk.models.transaction_response import TransactionResponse
from moonsdk.models.transaction_response_tx import TransactionResponseTx
from typing import Optional, Set
from typing_extensions import Self

class ConveyorFinanceControllerResponse(BaseModel):
    """
    ConveyorFinanceControllerResponse
    """ # noqa: E501
    input: Optional[InputBody] = None
    convey: Optional[TransactionResponse] = None
    data: Optional[TransactionData] = None
    tx: Optional[TransactionResponseTx] = None
    signed: Optional[Transaction] = None
    success: StrictBool
    message: StrictStr
    __properties: ClassVar[List[str]] = ["input", "convey", "data", "tx", "signed", "success", "message"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ConveyorFinanceControllerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of input
        if self.input:
            _dict['input'] = self.input.to_dict()
        # override the default output from pydantic by calling `to_dict()` of convey
        if self.convey:
            _dict['convey'] = self.convey.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tx
        if self.tx:
            _dict['tx'] = self.tx.to_dict()
        # override the default output from pydantic by calling `to_dict()` of signed
        if self.signed:
            _dict['signed'] = self.signed.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConveyorFinanceControllerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "input": InputBody.from_dict(obj["input"]) if obj.get("input") is not None else None,
            "convey": TransactionResponse.from_dict(obj["convey"]) if obj.get("convey") is not None else None,
            "data": TransactionData.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "tx": TransactionResponseTx.from_dict(obj["tx"]) if obj.get("tx") is not None else None,
            "signed": Transaction.from_dict(obj["signed"]) if obj.get("signed") is not None else None,
            "success": obj.get("success"),
            "message": obj.get("message")
        })
        return _obj


