# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from moonsdk.models.i_webhook import IWebhook

class TestIWebhook(unittest.TestCase):
    """IWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IWebhook:
        """Test IWebhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IWebhook`
        """
        model = IWebhook()
        if include_optional:
            return IWebhook(
                block = moonsdk.models.block.Block(
                    number = '', 
                    hash = '', 
                    timestamp = '', ),
                chain_id = '',
                logs = [
                    moonsdk.models.log.Log(
                        triggers = [
                            moonsdk.models.trigger_output.TriggerOutput(
                                value = null, 
                                name = '', )
                            ], 
                        log_index = '', 
                        transaction_hash = '', 
                        address = '', 
                        data = '', 
                        topic0 = '', 
                        topic1 = '', 
                        topic2 = '', 
                        topic3 = '', )
                    ],
                txs = [
                    moonsdk.models.transaction.Transaction(
                        transaction_hash = '', 
                        signed_transaction = '', 
                        raw_transaction = '', 
                        data = '', 
                        transactions = [
                            moonsdk.models.transaction_data.TransactionData(
                                moon_scan_url = '', 
                                transaction_hash = '', 
                                signed_transaction = '', 
                                signed_message = '', 
                                raw_transaction = '', 
                                signature = '', 
                                transaction = moonsdk.models.tx.Tx(
                                    type = 1.337, 
                                    chain_id = 1.337, 
                                    data = '', 
                                    gas = '', 
                                    gas_price = '', 
                                    gas_tip_cap = '', 
                                    gas_fee_cap = '', 
                                    value = '', 
                                    nonce = 1.337, 
                                    from = '', 
                                    to = '', 
                                    blob_gas = '', 
                                    blob_gas_fee_cap = '', 
                                    blob_hashes = [
                                        ''
                                        ], 
                                    v = '', 
                                    r = '', 
                                    s = '', ), 
                                user_ops = [
                                    moonsdk.models.transaction_request.TransactionRequest(
                                        nonce = '', 
                                        data = '', 
                                        value = '', 
                                        to = '', 
                                        from = '', 
                                        max_fee_per_gas = '', 
                                        max_priority_fee_per_gas = '', )
                                    ], 
                                userop_transaction = '', )
                            ], 
                        moon_scan_url = '', 
                        signature = '', 
                        transaction = moonsdk.models.tx.Tx(
                            type = 1.337, 
                            chain_id = 1.337, 
                            data = '', 
                            gas = '', 
                            gas_price = '', 
                            gas_tip_cap = '', 
                            gas_fee_cap = '', 
                            value = '', 
                            nonce = 1.337, 
                            from = '', 
                            to = '', 
                            blob_gas = '', 
                            blob_gas_fee_cap = '', 
                            v = '', 
                            r = '', 
                            s = '', ), 
                        user_ops = [
                            moonsdk.models.transaction_request.TransactionRequest(
                                nonce = '', 
                                data = '', 
                                value = '', 
                                to = '', 
                                from = '', 
                                max_fee_per_gas = '', 
                                max_priority_fee_per_gas = '', )
                            ], 
                        userop_transaction = '', )
                    ],
                txs_internal = [
                    moonsdk.models.internal_transaction.InternalTransaction(
                        from = '', 
                        to = '', 
                        value = '', 
                        transaction_hash = '', 
                        gas = '', )
                    ],
                abi = [
                    {}
                    ],
                retries = 1.337,
                confirmed = True,
                tag = '',
                stream_id = '',
                erc20_transfers = [
                    moonsdk.models.ierc20_transfer.IERC20Transfer(
                        transaction_hash = '', 
                        contract = '', 
                        log_index = '', 
                        from = '', 
                        to = '', 
                        value = '', 
                        token_decimals = '', 
                        token_name = '', 
                        token_symbol = '', 
                        value_with_decimals = '', 
                        triggers = [
                            moonsdk.models.trigger_output.TriggerOutput(
                                value = null, 
                                name = '', )
                            ], )
                    ],
                erc20_approvals = [
                    moonsdk.models.ierc20_approval.IERC20Approval(
                        transaction_hash = '', 
                        contract = '', 
                        log_index = '', 
                        owner = '', 
                        spender = '', 
                        value = '', 
                        token_decimals = '', 
                        token_name = '', 
                        token_symbol = '', 
                        value_with_decimals = '', 
                        triggers = [
                            moonsdk.models.trigger_output.TriggerOutput(
                                value = null, 
                                name = '', )
                            ], )
                    ],
                nft_transfers = [
                    moonsdk.models.inft_transfer.INFTTransfer(
                        transaction_hash = '', 
                        contract = '', 
                        log_index = '', 
                        token_contract_type = '', 
                        token_name = '', 
                        token_symbol = '', 
                        triggers = [
                            moonsdk.models.trigger_output.TriggerOutput(
                                value = null, 
                                name = '', )
                            ], 
                        operator = '', 
                        from = '', 
                        to = '', 
                        token_id = '', 
                        amount = '', )
                    ],
                native_balances = [
                    moonsdk.models.i_native_balance.INativeBalance(
                        address = '', 
                        balance = '', )
                    ],
                nft_approvals = moonsdk.models.i_old_nft_approval.IOldNFTApproval(
                    erc721 = [
                        moonsdk.models.inft_approval_erc721.INFTApprovalERC721(
                            transaction_hash = '', 
                            contract = '', 
                            log_index = '', 
                            owner = '', 
                            approved = '', 
                            token_id = '', 
                            token_contract_type = '', 
                            token_name = '', 
                            token_symbol = '', )
                        ], 
                    erc1155 = [
                        moonsdk.models.inft_approval_erc1155.INFTApprovalERC1155(
                            transaction_hash = '', 
                            contract = '', 
                            log_index = '', 
                            account = '', 
                            operator = '', 
                            approved = True, 
                            token_contract_type = '', 
                            token_name = '', 
                            token_symbol = '', )
                        ], ),
                nft_token_approvals = [
                    moonsdk.models.inft_approval.INFTApproval(
                        transaction_hash = '', 
                        contract = '', 
                        log_index = '', 
                        token_contract_type = '', 
                        token_name = '', 
                        token_symbol = '', 
                        account = '', 
                        operator = '', 
                        approved_all = True, 
                        token_id = '', )
                    ]
            )
        else:
            return IWebhook(
                block = moonsdk.models.block.Block(
                    number = '', 
                    hash = '', 
                    timestamp = '', ),
                chain_id = '',
                logs = [
                    moonsdk.models.log.Log(
                        triggers = [
                            moonsdk.models.trigger_output.TriggerOutput(
                                value = null, 
                                name = '', )
                            ], 
                        log_index = '', 
                        transaction_hash = '', 
                        address = '', 
                        data = '', 
                        topic0 = '', 
                        topic1 = '', 
                        topic2 = '', 
                        topic3 = '', )
                    ],
                txs = [
                    moonsdk.models.transaction.Transaction(
                        transaction_hash = '', 
                        signed_transaction = '', 
                        raw_transaction = '', 
                        data = '', 
                        transactions = [
                            moonsdk.models.transaction_data.TransactionData(
                                moon_scan_url = '', 
                                transaction_hash = '', 
                                signed_transaction = '', 
                                signed_message = '', 
                                raw_transaction = '', 
                                signature = '', 
                                transaction = moonsdk.models.tx.Tx(
                                    type = 1.337, 
                                    chain_id = 1.337, 
                                    data = '', 
                                    gas = '', 
                                    gas_price = '', 
                                    gas_tip_cap = '', 
                                    gas_fee_cap = '', 
                                    value = '', 
                                    nonce = 1.337, 
                                    from = '', 
                                    to = '', 
                                    blob_gas = '', 
                                    blob_gas_fee_cap = '', 
                                    blob_hashes = [
                                        ''
                                        ], 
                                    v = '', 
                                    r = '', 
                                    s = '', ), 
                                user_ops = [
                                    moonsdk.models.transaction_request.TransactionRequest(
                                        nonce = '', 
                                        data = '', 
                                        value = '', 
                                        to = '', 
                                        from = '', 
                                        max_fee_per_gas = '', 
                                        max_priority_fee_per_gas = '', )
                                    ], 
                                userop_transaction = '', )
                            ], 
                        moon_scan_url = '', 
                        signature = '', 
                        transaction = moonsdk.models.tx.Tx(
                            type = 1.337, 
                            chain_id = 1.337, 
                            data = '', 
                            gas = '', 
                            gas_price = '', 
                            gas_tip_cap = '', 
                            gas_fee_cap = '', 
                            value = '', 
                            nonce = 1.337, 
                            from = '', 
                            to = '', 
                            blob_gas = '', 
                            blob_gas_fee_cap = '', 
                            v = '', 
                            r = '', 
                            s = '', ), 
                        user_ops = [
                            moonsdk.models.transaction_request.TransactionRequest(
                                nonce = '', 
                                data = '', 
                                value = '', 
                                to = '', 
                                from = '', 
                                max_fee_per_gas = '', 
                                max_priority_fee_per_gas = '', )
                            ], 
                        userop_transaction = '', )
                    ],
                txs_internal = [
                    moonsdk.models.internal_transaction.InternalTransaction(
                        from = '', 
                        to = '', 
                        value = '', 
                        transaction_hash = '', 
                        gas = '', )
                    ],
                abi = [
                    {}
                    ],
                retries = 1.337,
                confirmed = True,
                tag = '',
                stream_id = '',
                erc20_transfers = [
                    moonsdk.models.ierc20_transfer.IERC20Transfer(
                        transaction_hash = '', 
                        contract = '', 
                        log_index = '', 
                        from = '', 
                        to = '', 
                        value = '', 
                        token_decimals = '', 
                        token_name = '', 
                        token_symbol = '', 
                        value_with_decimals = '', 
                        triggers = [
                            moonsdk.models.trigger_output.TriggerOutput(
                                value = null, 
                                name = '', )
                            ], )
                    ],
                erc20_approvals = [
                    moonsdk.models.ierc20_approval.IERC20Approval(
                        transaction_hash = '', 
                        contract = '', 
                        log_index = '', 
                        owner = '', 
                        spender = '', 
                        value = '', 
                        token_decimals = '', 
                        token_name = '', 
                        token_symbol = '', 
                        value_with_decimals = '', 
                        triggers = [
                            moonsdk.models.trigger_output.TriggerOutput(
                                value = null, 
                                name = '', )
                            ], )
                    ],
                nft_transfers = [
                    moonsdk.models.inft_transfer.INFTTransfer(
                        transaction_hash = '', 
                        contract = '', 
                        log_index = '', 
                        token_contract_type = '', 
                        token_name = '', 
                        token_symbol = '', 
                        triggers = [
                            moonsdk.models.trigger_output.TriggerOutput(
                                value = null, 
                                name = '', )
                            ], 
                        operator = '', 
                        from = '', 
                        to = '', 
                        token_id = '', 
                        amount = '', )
                    ],
                native_balances = [
                    moonsdk.models.i_native_balance.INativeBalance(
                        address = '', 
                        balance = '', )
                    ],
                nft_approvals = moonsdk.models.i_old_nft_approval.IOldNFTApproval(
                    erc721 = [
                        moonsdk.models.inft_approval_erc721.INFTApprovalERC721(
                            transaction_hash = '', 
                            contract = '', 
                            log_index = '', 
                            owner = '', 
                            approved = '', 
                            token_id = '', 
                            token_contract_type = '', 
                            token_name = '', 
                            token_symbol = '', )
                        ], 
                    erc1155 = [
                        moonsdk.models.inft_approval_erc1155.INFTApprovalERC1155(
                            transaction_hash = '', 
                            contract = '', 
                            log_index = '', 
                            account = '', 
                            operator = '', 
                            approved = True, 
                            token_contract_type = '', 
                            token_name = '', 
                            token_symbol = '', )
                        ], ),
                nft_token_approvals = [
                    moonsdk.models.inft_approval.INFTApproval(
                        transaction_hash = '', 
                        contract = '', 
                        log_index = '', 
                        token_contract_type = '', 
                        token_name = '', 
                        token_symbol = '', 
                        account = '', 
                        operator = '', 
                        approved_all = True, 
                        token_id = '', )
                    ],
        )
        """

    def testIWebhook(self):
        """Test IWebhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
