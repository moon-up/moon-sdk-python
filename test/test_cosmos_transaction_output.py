# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.cosmos_transaction_output import CosmosTransactionOutput

class TestCosmosTransactionOutput(unittest.TestCase):
    """CosmosTransactionOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CosmosTransactionOutput:
        """Test CosmosTransactionOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CosmosTransactionOutput`
        """
        model = CosmosTransactionOutput()
        if include_optional:
            return CosmosTransactionOutput(
                signed_tx = '',
                transaction_hash = ''
            )
        else:
            return CosmosTransactionOutput(
        )
        """

    def testCosmosTransactionOutput(self):
        """Test CosmosTransactionOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
