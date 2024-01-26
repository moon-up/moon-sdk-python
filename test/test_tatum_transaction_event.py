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

from moonsdk.models.tatum_transaction_event import TatumTransactionEvent

class TestTatumTransactionEvent(unittest.TestCase):
    """TatumTransactionEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TatumTransactionEvent:
        """Test TatumTransactionEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TatumTransactionEvent`
        """
        model = TatumTransactionEvent()
        if include_optional:
            return TatumTransactionEvent(
                amount = '',
                test = True,
                counter_address = '',
                address = '',
                mempool = True,
                subscription_type = '',
                block_number = 1.337,
                tx_id = '',
                chain = '',
                currency = ''
            )
        else:
            return TatumTransactionEvent(
                amount = '',
                test = True,
                counter_address = '',
                address = '',
                mempool = True,
                subscription_type = '',
                block_number = 1.337,
                tx_id = '',
                chain = '',
                currency = '',
        )
        """

    def testTatumTransactionEvent(self):
        """Test TatumTransactionEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()