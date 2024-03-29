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


from typing import Any, ClassVar, Dict, List, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from moonsdk.models.abi_item import AbiItem
from moonsdk.models.block import Block
from moonsdk.models.i_native_balance import INativeBalance
from moonsdk.models.i_old_nft_approval import IOldNFTApproval
from moonsdk.models.ierc20_approval import IERC20Approval
from moonsdk.models.ierc20_transfer import IERC20Transfer
from moonsdk.models.inft_approval import INFTApproval
from moonsdk.models.inft_transfer import INFTTransfer
from moonsdk.models.internal_transaction import InternalTransaction
from moonsdk.models.log import Log
from moonsdk.models.transaction import Transaction
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IWebhook(BaseModel):
    """
    IWebhook
    """ # noqa: E501
    block: Block
    chain_id: StrictStr = Field(alias="chainId")
    logs: List[Log]
    txs: List[Transaction]
    txs_internal: List[InternalTransaction] = Field(alias="txsInternal")
    abi: List[AbiItem]
    retries: Union[StrictFloat, StrictInt]
    confirmed: StrictBool
    tag: StrictStr
    stream_id: StrictStr = Field(alias="streamId")
    erc20_transfers: List[IERC20Transfer] = Field(alias="erc20Transfers")
    erc20_approvals: List[IERC20Approval] = Field(alias="erc20Approvals")
    nft_transfers: List[INFTTransfer] = Field(alias="nftTransfers")
    native_balances: List[INativeBalance] = Field(alias="nativeBalances")
    nft_approvals: IOldNFTApproval = Field(alias="nftApprovals")
    nft_token_approvals: List[INFTApproval] = Field(alias="nftTokenApprovals")
    __properties: ClassVar[List[str]] = ["block", "chainId", "logs", "txs", "txsInternal", "abi", "retries", "confirmed", "tag", "streamId", "erc20Transfers", "erc20Approvals", "nftTransfers", "nativeBalances", "nftApprovals", "nftTokenApprovals"]

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
        """Create an instance of IWebhook from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of block
        if self.block:
            _dict['block'] = self.block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in logs (list)
        _items = []
        if self.logs:
            for _item in self.logs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['logs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in txs (list)
        _items = []
        if self.txs:
            for _item in self.txs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['txs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in txs_internal (list)
        _items = []
        if self.txs_internal:
            for _item in self.txs_internal:
                if _item:
                    _items.append(_item.to_dict())
            _dict['txsInternal'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in abi (list)
        _items = []
        if self.abi:
            for _item in self.abi:
                if _item:
                    _items.append(_item.to_dict())
            _dict['abi'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in erc20_transfers (list)
        _items = []
        if self.erc20_transfers:
            for _item in self.erc20_transfers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['erc20Transfers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in erc20_approvals (list)
        _items = []
        if self.erc20_approvals:
            for _item in self.erc20_approvals:
                if _item:
                    _items.append(_item.to_dict())
            _dict['erc20Approvals'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nft_transfers (list)
        _items = []
        if self.nft_transfers:
            for _item in self.nft_transfers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nftTransfers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in native_balances (list)
        _items = []
        if self.native_balances:
            for _item in self.native_balances:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nativeBalances'] = _items
        # override the default output from pydantic by calling `to_dict()` of nft_approvals
        if self.nft_approvals:
            _dict['nftApprovals'] = self.nft_approvals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in nft_token_approvals (list)
        _items = []
        if self.nft_token_approvals:
            for _item in self.nft_token_approvals:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nftTokenApprovals'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "block": Block.from_dict(obj.get("block")) if obj.get("block") is not None else None,
            "chainId": obj.get("chainId"),
            "logs": [Log.from_dict(_item) for _item in obj.get("logs")] if obj.get("logs") is not None else None,
            "txs": [Transaction.from_dict(_item) for _item in obj.get("txs")] if obj.get("txs") is not None else None,
            "txsInternal": [InternalTransaction.from_dict(_item) for _item in obj.get("txsInternal")] if obj.get("txsInternal") is not None else None,
            "abi": [AbiItem.from_dict(_item) for _item in obj.get("abi")] if obj.get("abi") is not None else None,
            "retries": obj.get("retries"),
            "confirmed": obj.get("confirmed"),
            "tag": obj.get("tag"),
            "streamId": obj.get("streamId"),
            "erc20Transfers": [IERC20Transfer.from_dict(_item) for _item in obj.get("erc20Transfers")] if obj.get("erc20Transfers") is not None else None,
            "erc20Approvals": [IERC20Approval.from_dict(_item) for _item in obj.get("erc20Approvals")] if obj.get("erc20Approvals") is not None else None,
            "nftTransfers": [INFTTransfer.from_dict(_item) for _item in obj.get("nftTransfers")] if obj.get("nftTransfers") is not None else None,
            "nativeBalances": [INativeBalance.from_dict(_item) for _item in obj.get("nativeBalances")] if obj.get("nativeBalances") is not None else None,
            "nftApprovals": IOldNFTApproval.from_dict(obj.get("nftApprovals")) if obj.get("nftApprovals") is not None else None,
            "nftTokenApprovals": [INFTApproval.from_dict(_item) for _item in obj.get("nftTokenApprovals")] if obj.get("nftTokenApprovals") is not None else None
        })
        return _obj


