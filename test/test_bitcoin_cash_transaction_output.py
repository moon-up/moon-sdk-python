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

from moonsdk.models.bitcoin_cash_transaction_output import BitcoinCashTransactionOutput

class TestBitcoinCashTransactionOutput(unittest.TestCase):
    """BitcoinCashTransactionOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BitcoinCashTransactionOutput:
        """Test BitcoinCashTransactionOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BitcoinCashTransactionOutput`
        """
        model = BitcoinCashTransactionOutput()
        if include_optional:
            return BitcoinCashTransactionOutput(
                signed_tx = '',
                transaction_hash = ''
            )
        else:
            return BitcoinCashTransactionOutput(
        )
        """

    def testBitcoinCashTransactionOutput(self):
        """Test BitcoinCashTransactionOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()