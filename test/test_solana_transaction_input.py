# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.solana_transaction_input import SolanaTransactionInput

class TestSolanaTransactionInput(unittest.TestCase):
    """SolanaTransactionInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SolanaTransactionInput:
        """Test SolanaTransactionInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SolanaTransactionInput`
        """
        model = SolanaTransactionInput()
        if include_optional:
            return SolanaTransactionInput(
                to = '',
                value = 1.337,
                network = '',
                compress = True
            )
        else:
            return SolanaTransactionInput(
        )
        """

    def testSolanaTransactionInput(self):
        """Test SolanaTransactionInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
