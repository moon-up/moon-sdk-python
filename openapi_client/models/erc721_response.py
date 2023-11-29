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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Erc721Response(BaseModel):
    """
    Erc721Response
    """ # noqa: E501
    type: Optional[Union[StrictFloat, StrictInt]] = None
    chain_id: Optional[Union[StrictFloat, StrictInt]] = None
    data: Optional[StrictStr] = None
    gas: Optional[StrictStr] = None
    gas_price: Optional[StrictStr] = None
    gas_tip_cap: Optional[StrictStr] = None
    gas_fee_cap: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    nonce: Optional[Union[StrictFloat, StrictInt]] = None
    var_from: Optional[StrictStr] = Field(default=None, alias="from")
    to: Optional[StrictStr] = None
    blob_gas: Optional[StrictStr] = None
    blob_gas_fee_cap: Optional[StrictStr] = None
    blob_hashes: Optional[List[StrictStr]] = None
    v: Optional[StrictStr] = None
    r: Optional[StrictStr] = None
    s: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    symbol: Optional[StrictStr] = None
    balance_of: Optional[StrictStr] = None
    owner_of: Optional[StrictStr] = None
    token_uri: Optional[StrictStr] = None
    contract_address: Optional[StrictStr] = None
    is_approved_for_all: Optional[StrictStr] = Field(default=None, alias="isApprovedForAll")
    __properties: ClassVar[List[str]] = ["type", "chain_id", "data", "gas", "gas_price", "gas_tip_cap", "gas_fee_cap", "value", "nonce", "from", "to", "blob_gas", "blob_gas_fee_cap", "blob_hashes", "v", "r", "s", "name", "symbol", "balance_of", "owner_of", "token_uri", "contract_address", "isApprovedForAll"]

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
        """Create an instance of Erc721Response from a JSON string"""
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
        # set to None if gas_tip_cap (nullable) is None
        # and model_fields_set contains the field
        if self.gas_tip_cap is None and "gas_tip_cap" in self.model_fields_set:
            _dict['gas_tip_cap'] = None

        # set to None if gas_fee_cap (nullable) is None
        # and model_fields_set contains the field
        if self.gas_fee_cap is None and "gas_fee_cap" in self.model_fields_set:
            _dict['gas_fee_cap'] = None

        # set to None if to (nullable) is None
        # and model_fields_set contains the field
        if self.to is None and "to" in self.model_fields_set:
            _dict['to'] = None

        # set to None if blob_gas (nullable) is None
        # and model_fields_set contains the field
        if self.blob_gas is None and "blob_gas" in self.model_fields_set:
            _dict['blob_gas'] = None

        # set to None if blob_gas_fee_cap (nullable) is None
        # and model_fields_set contains the field
        if self.blob_gas_fee_cap is None and "blob_gas_fee_cap" in self.model_fields_set:
            _dict['blob_gas_fee_cap'] = None

        # set to None if blob_hashes (nullable) is None
        # and model_fields_set contains the field
        if self.blob_hashes is None and "blob_hashes" in self.model_fields_set:
            _dict['blob_hashes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Erc721Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "chain_id": obj.get("chain_id"),
            "data": obj.get("data"),
            "gas": obj.get("gas"),
            "gas_price": obj.get("gas_price"),
            "gas_tip_cap": obj.get("gas_tip_cap"),
            "gas_fee_cap": obj.get("gas_fee_cap"),
            "value": obj.get("value"),
            "nonce": obj.get("nonce"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "blob_gas": obj.get("blob_gas"),
            "blob_gas_fee_cap": obj.get("blob_gas_fee_cap"),
            "blob_hashes": obj.get("blob_hashes"),
            "v": obj.get("v"),
            "r": obj.get("r"),
            "s": obj.get("s"),
            "name": obj.get("name"),
            "symbol": obj.get("symbol"),
            "balance_of": obj.get("balance_of"),
            "owner_of": obj.get("owner_of"),
            "token_uri": obj.get("token_uri"),
            "contract_address": obj.get("contract_address"),
            "isApprovedForAll": obj.get("isApprovedForAll")
        })
        return _obj


