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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class AaveReservesData(BaseModel):
    """
    AaveReservesData
    """ # noqa: E501
    current_atoken_balance: StrictStr
    current_borrow_balance: StrictStr
    principal_borrow_balance: StrictStr
    borrow_rate_mode: StrictStr
    borrow_rate: StrictStr
    liquidity_rate: StrictStr
    origination_fee: StrictStr
    variable_borrow_index: StrictStr
    last_update_timestamp: StrictStr
    usage_as_collateral_enabled: StrictStr
    __properties: ClassVar[List[str]] = ["current_atoken_balance", "current_borrow_balance", "principal_borrow_balance", "borrow_rate_mode", "borrow_rate", "liquidity_rate", "origination_fee", "variable_borrow_index", "last_update_timestamp", "usage_as_collateral_enabled"]

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
        """Create an instance of AaveReservesData from a JSON string"""
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
        """Create an instance of AaveReservesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current_atoken_balance": obj.get("current_atoken_balance"),
            "current_borrow_balance": obj.get("current_borrow_balance"),
            "principal_borrow_balance": obj.get("principal_borrow_balance"),
            "borrow_rate_mode": obj.get("borrow_rate_mode"),
            "borrow_rate": obj.get("borrow_rate"),
            "liquidity_rate": obj.get("liquidity_rate"),
            "origination_fee": obj.get("origination_fee"),
            "variable_borrow_index": obj.get("variable_borrow_index"),
            "last_update_timestamp": obj.get("last_update_timestamp"),
            "usage_as_collateral_enabled": obj.get("usage_as_collateral_enabled")
        })
        return _obj


