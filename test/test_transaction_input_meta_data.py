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

from openapi_client.models.transaction_input_meta_data import TransactionInputMetaData

class TestTransactionInputMetaData(unittest.TestCase):
    """TransactionInputMetaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionInputMetaData:
        """Test TransactionInputMetaData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionInputMetaData`
        """
        model = TransactionInputMetaData()
        if include_optional:
            return TransactionInputMetaData(
                quote_id = ''
            )
        else:
            return TransactionInputMetaData(
                quote_id = '',
        )
        """

    def testTransactionInputMetaData(self):
        """Test TransactionInputMetaData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()