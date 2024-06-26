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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from moonsdk.models.transaction_response_info import TransactionResponseInfo
from moonsdk.models.transaction_response_tx import TransactionResponseTx
from typing import Optional, Set
from typing_extensions import Self

class TransactionResponse(BaseModel):
    """
    TransactionResponse
    """ # noqa: E501
    message: StrictStr
    tx: TransactionResponseTx
    info: TransactionResponseInfo
    chain_id: Union[StrictFloat, StrictInt] = Field(alias="chainId")
    current_block_number: Union[StrictFloat, StrictInt] = Field(alias="currentBlockNumber")
    __properties: ClassVar[List[str]] = ["message", "tx", "info", "chainId", "currentBlockNumber"]

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
        """Create an instance of TransactionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tx
        if self.tx:
            _dict['tx'] = self.tx.to_dict()
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "tx": TransactionResponseTx.from_dict(obj["tx"]) if obj.get("tx") is not None else None,
            "info": TransactionResponseInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "chainId": obj.get("chainId"),
            "currentBlockNumber": obj.get("currentBlockNumber")
        })
        return _obj


