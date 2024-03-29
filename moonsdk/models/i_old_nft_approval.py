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
from pydantic import Field
from moonsdk.models.inft_approval_erc1155 import INFTApprovalERC1155
from moonsdk.models.inft_approval_erc721 import INFTApprovalERC721
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IOldNFTApproval(BaseModel):
    """
    IOldNFTApproval
    """ # noqa: E501
    erc721: List[INFTApprovalERC721] = Field(alias="ERC721")
    erc1155: List[INFTApprovalERC1155] = Field(alias="ERC1155")
    __properties: ClassVar[List[str]] = ["ERC721", "ERC1155"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
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
        """Create an instance of IOldNFTApproval from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in erc721 (list)
        _items = []
        if self.erc721:
            for _item in self.erc721:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ERC721'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in erc1155 (list)
        _items = []
        if self.erc1155:
            for _item in self.erc1155:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ERC1155'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IOldNFTApproval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ERC721": [INFTApprovalERC721.from_dict(_item) for _item in obj.get("ERC721")] if obj.get("ERC721") is not None else None,
            "ERC1155": [INFTApprovalERC1155.from_dict(_item) for _item in obj.get("ERC1155")] if obj.get("ERC1155") is not None else None
        })
        return _obj


