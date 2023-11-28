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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from openapi_client.models.crypto_currency import CryptoCurrency
from openapi_client.models.fiat_currency import FiatCurrency
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Message(BaseModel):
    """
    Message
    """ # noqa: E501
    fiat: List[FiatCurrency]
    crypto: List[CryptoCurrency]
    __properties: ClassVar[List[str]] = ["fiat", "crypto"]

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
        """Create an instance of Message from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fiat (list)
        _items = []
        if self.fiat:
            for _item in self.fiat:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fiat'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in crypto (list)
        _items = []
        if self.crypto:
            for _item in self.crypto:
                if _item:
                    _items.append(_item.to_dict())
            _dict['crypto'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Message from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fiat": [FiatCurrency.from_dict(_item) for _item in obj.get("fiat")] if obj.get("fiat") is not None else None,
            "crypto": [CryptoCurrency.from_dict(_item) for _item in obj.get("crypto")] if obj.get("crypto") is not None else None
        })
        return _obj


