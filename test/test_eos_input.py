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

from openapi_client.models.eos_input import EosInput

class TestEosInput(unittest.TestCase):
    """EosInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EosInput:
        """Test EosInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EosInput`
        """
        model = EosInput()
        if include_optional:
            return EosInput(
                network = '',
                private_key = ''
            )
        else:
            return EosInput(
        )
        """

    def testEosInput(self):
        """Test EosInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
