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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.transaction_data import TransactionData
from openapi_client.models.transaction_request import TransactionRequest
from openapi_client.models.tx import Tx
from typing import Optional, Set
from typing_extensions import Self

class Transaction(BaseModel):
    """
    Transaction
    """ # noqa: E501
    transaction_hash: Optional[StrictStr] = None
    signed_transaction: Optional[StrictStr] = None
    raw_transaction: Optional[StrictStr] = None
    data: Optional[StrictStr] = None
    transactions: Optional[List[TransactionData]] = None
    moon_scan_url: Optional[StrictStr] = None
    signature: Optional[StrictStr] = None
    transaction: Optional[Tx] = None
    user_ops: Optional[List[TransactionRequest]] = Field(default=None, alias="userOps")
    userop_transaction: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["transaction_hash", "signed_transaction", "raw_transaction", "data", "transactions", "moon_scan_url", "signature", "transaction", "userOps", "userop_transaction"]

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
        """Create an instance of Transaction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in user_ops (list)
        _items = []
        if self.user_ops:
            for _item in self.user_ops:
                if _item:
                    _items.append(_item.to_dict())
            _dict['userOps'] = _items
        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Transaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transaction_hash": obj.get("transaction_hash"),
            "signed_transaction": obj.get("signed_transaction"),
            "raw_transaction": obj.get("raw_transaction"),
            "data": obj.get("data"),
            "transactions": [TransactionData.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None,
            "moon_scan_url": obj.get("moon_scan_url"),
            "signature": obj.get("signature"),
            "transaction": Tx.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "userOps": [TransactionRequest.from_dict(_item) for _item in obj["userOps"]] if obj.get("userOps") is not None else None,
            "userop_transaction": obj.get("userop_transaction")
        })
        return _obj


