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

from openapi_client.models.transaction_response_info import TransactionResponseInfo

class TestTransactionResponseInfo(unittest.TestCase):
    """TransactionResponseInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionResponseInfo:
        """Test TransactionResponseInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionResponseInfo`
        """
        model = TransactionResponseInfo()
        if include_optional:
            return TransactionResponseInfo(
                conveyor_gas = '',
                affiliate_gas = '',
                affiliate_aggregator = '',
                amount_out = '',
                amount_out_min = ''
            )
        else:
            return TransactionResponseInfo(
                conveyor_gas = '',
                affiliate_gas = '',
                affiliate_aggregator = '',
                amount_out = '',
                amount_out_min = '',
        )
        """

    def testTransactionResponseInfo(self):
        """Test TransactionResponseInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()