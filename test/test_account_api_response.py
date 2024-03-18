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

from moonsdk.models.account_api_response import AccountAPIResponse

class TestAccountAPIResponse(unittest.TestCase):
    """AccountAPIResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountAPIResponse:
        """Test AccountAPIResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountAPIResponse`
        """
        model = AccountAPIResponse()
        if include_optional:
            return AccountAPIResponse(
                success = True,
                message = '',
                data = moonsdk.models.account_response.AccountResponse(
                    data = moonsdk.models.account_data.AccountData(
                        keys = [
                            ''
                            ], 
                        address = '', ), )
            )
        else:
            return AccountAPIResponse(
                success = True,
                message = '',
        )
        """

    def testAccountAPIResponse(self):
        """Test AccountAPIResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
