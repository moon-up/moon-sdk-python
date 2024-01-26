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

from moonsdk.models.uniswap_input import UniswapInput

class TestUniswapInput(unittest.TestCase):
    """UniswapInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UniswapInput:
        """Test UniswapInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UniswapInput`
        """
        model = UniswapInput()
        if include_optional:
            return UniswapInput(
                to = '',
                data = '',
                input = '',
                value = '',
                nonce = '',
                gas = '',
                gas_price = '',
                chain_id = '',
                encoding = '',
                eoa = True,
                contract_address = '',
                token_id = '',
                token_ids = '',
                approved = True,
                broadcast = True,
                token_a = '',
                token_b = '',
                amount_a = '',
                amount_b = ''
            )
        else:
            return UniswapInput(
        )
        """

    def testUniswapInput(self):
        """Test UniswapInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
