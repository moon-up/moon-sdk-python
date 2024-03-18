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

from moonsdk.models.tron_transaction_output import TronTransactionOutput

class TestTronTransactionOutput(unittest.TestCase):
    """TronTransactionOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TronTransactionOutput:
        """Test TronTransactionOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TronTransactionOutput`
        """
        model = TronTransactionOutput()
        if include_optional:
            return TronTransactionOutput(
                signed_tx = '',
                transaction_hash = ''
            )
        else:
            return TronTransactionOutput(
        )
        """

    def testTronTransactionOutput(self):
        """Test TronTransactionOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()