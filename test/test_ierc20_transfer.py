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

from openapi_client.models.ierc20_transfer import IERC20Transfer

class TestIERC20Transfer(unittest.TestCase):
    """IERC20Transfer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IERC20Transfer:
        """Test IERC20Transfer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IERC20Transfer`
        """
        model = IERC20Transfer()
        if include_optional:
            return IERC20Transfer(
                transaction_hash = '',
                contract = '',
                log_index = '',
                var_from = '',
                to = '',
                value = '',
                token_decimals = '',
                token_name = '',
                token_symbol = '',
                value_with_decimals = '',
                triggers = [
                    openapi_client.models.trigger_output.TriggerOutput(
                        value = null, 
                        name = '', )
                    ]
            )
        else:
            return IERC20Transfer(
                transaction_hash = '',
                contract = '',
                log_index = '',
                var_from = '',
                to = '',
                value = '',
                token_decimals = '',
                token_name = '',
                token_symbol = '',
        )
        """

    def testIERC20Transfer(self):
        """Test IERC20Transfer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()