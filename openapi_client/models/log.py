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

class Log(BaseModel):
    """
    Log
    """ # noqa: E501
    triggers: Optional[List[TriggerOutput]] = None
    log_index: StrictStr = Field(alias="logIndex")
    transaction_hash: StrictStr = Field(alias="transactionHash")
    address: StrictStr
    data: StrictStr
    topic0: Optional[StrictStr]
    topic1: Optional[StrictStr]
    topic2: Optional[StrictStr]
    topic3: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["triggers", "logIndex", "transactionHash", "address", "data", "topic0", "topic1", "topic2", "topic3"]

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
        """Create an instance of Log from a JSON string"""
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
        # set to None if topic0 (nullable) is None
        # and model_fields_set contains the field
        if self.topic0 is None and "topic0" in self.model_fields_set:
            _dict['topic0'] = None

        # set to None if topic1 (nullable) is None
        # and model_fields_set contains the field
        if self.topic1 is None and "topic1" in self.model_fields_set:
            _dict['topic1'] = None

        # set to None if topic2 (nullable) is None
        # and model_fields_set contains the field
        if self.topic2 is None and "topic2" in self.model_fields_set:
            _dict['topic2'] = None

        # set to None if topic3 (nullable) is None
        # and model_fields_set contains the field
        if self.topic3 is None and "topic3" in self.model_fields_set:
            _dict['topic3'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Log from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "triggers": [TriggerOutput.from_dict(_item) for _item in obj.get("triggers")] if obj.get("triggers") is not None else None,
            "logIndex": obj.get("logIndex"),
            "transactionHash": obj.get("transactionHash"),
            "address": obj.get("address"),
            "data": obj.get("data"),
            "topic0": obj.get("topic0"),
            "topic1": obj.get("topic1"),
            "topic2": obj.get("topic2"),
            "topic3": obj.get("topic3")
        })
        return _obj


