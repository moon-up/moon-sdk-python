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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UniswapInput(BaseModel):
    """
    UniswapInput
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
    token_a: Optional[StrictStr] = None
    token_b: Optional[StrictStr] = None
    amount_a: Optional[StrictStr] = None
    amount_b: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["to", "data", "input", "value", "nonce", "gas", "gasPrice", "chain_id", "encoding", "EOA", "contract_address", "token_id", "token_ids", "approved", "broadcast", "token_a", "token_b", "amount_a", "amount_b"]

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
        """Create an instance of UniswapInput from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UniswapInput from a dict"""
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
            "token_a": obj.get("token_a"),
            "token_b": obj.get("token_b"),
            "amount_a": obj.get("amount_a"),
            "amount_b": obj.get("amount_b")
        })
        return _obj


