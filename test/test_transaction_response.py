# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.transaction_response import TransactionResponse

class TestTransactionResponse(unittest.TestCase):
    """TransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionResponse:
        """Test TransactionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionResponse`
        """
        model = TransactionResponse()
        if include_optional:
            return TransactionResponse(
                message = '',
                tx = moonsdk.models.transaction_response_tx.TransactionResponse_tx(
                    data = '', 
                    value = '', 
                    nonce = 1.337, 
                    gas = '', 
                    to = '', 
                    from = '', ),
                info = moonsdk.models.transaction_response_info.TransactionResponse_info(
                    conveyor_gas = '', 
                    affiliate_gas = '', 
                    affiliate_aggregator = '', 
                    amount_out = '', 
                    amount_out_min = '', ),
                chain_id = 1.337,
                current_block_number = 1.337
            )
        else:
            return TransactionResponse(
                message = '',
                tx = moonsdk.models.transaction_response_tx.TransactionResponse_tx(
                    data = '', 
                    value = '', 
                    nonce = 1.337, 
                    gas = '', 
                    to = '', 
                    from = '', ),
                info = moonsdk.models.transaction_response_info.TransactionResponse_info(
                    conveyor_gas = '', 
                    affiliate_gas = '', 
                    affiliate_aggregator = '', 
                    amount_out = '', 
                    amount_out_min = '', ),
                chain_id = 1.337,
                current_block_number = 1.337,
        )
        """

    def testTransactionResponse(self):
        """Test TransactionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
