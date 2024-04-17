# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    """Transaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Transaction:
        """Test Transaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Transaction`
        """
        model = Transaction()
        if include_optional:
            return Transaction(
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
                userop_transaction = ''
            )
        else:
            return Transaction(
        )
        """

    def testTransaction(self):
        """Test Transaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
