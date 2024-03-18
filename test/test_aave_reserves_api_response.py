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

from moonsdk.models.aave_reserves_api_response import AaveReservesAPIResponse

class TestAaveReservesAPIResponse(unittest.TestCase):
    """AaveReservesAPIResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AaveReservesAPIResponse:
        """Test AaveReservesAPIResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AaveReservesAPIResponse`
        """
        model = AaveReservesAPIResponse()
        if include_optional:
            return AaveReservesAPIResponse(
                success = True,
                message = '',
                data = moonsdk.models.aave_reserves_data.AaveReservesData(
                    current_atoken_balance = '', 
                    current_borrow_balance = '', 
                    principal_borrow_balance = '', 
                    borrow_rate_mode = '', 
                    borrow_rate = '', 
                    liquidity_rate = '', 
                    origination_fee = '', 
                    variable_borrow_index = '', 
                    last_update_timestamp = '', 
                    usage_as_collateral_enabled = '', )
            )
        else:
            return AaveReservesAPIResponse(
                success = True,
                message = '',
        )
        """

    def testAaveReservesAPIResponse(self):
        """Test AaveReservesAPIResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()