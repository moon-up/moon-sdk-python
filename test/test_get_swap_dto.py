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

from moonsdk.models.get_swap_dto import GetSwapDto

class TestGetSwapDto(unittest.TestCase):
    """GetSwapDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSwapDto:
        """Test GetSwapDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSwapDto`
        """
        model = GetSwapDto()
        if include_optional:
            return GetSwapDto(
                src = '',
                dst = '',
                amount = '',
                var_from = '',
                slippage = 1.337,
                protocols = '',
                fee = '',
                disable_estimate = True,
                permit = '',
                include_tokens_info = True,
                include_protocols = True,
                compatibility = True,
                allow_partial_fill = True,
                parts = '',
                main_route_parts = '',
                connector_tokens = '',
                complexity_level = '',
                gas_limit = '',
                gas_price = '',
                referrer = '',
                receiver = '',
                chain_id = 1.337
            )
        else:
            return GetSwapDto(
                src = '',
                dst = '',
                amount = '',
                var_from = '',
                slippage = 1.337,
        )
        """

    def testGetSwapDto(self):
        """Test GetSwapDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
