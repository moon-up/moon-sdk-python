# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.create_account_input import CreateAccountInput

class TestCreateAccountInput(unittest.TestCase):
    """CreateAccountInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAccountInput:
        """Test CreateAccountInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAccountInput`
        """
        model = CreateAccountInput()
        if include_optional:
            return CreateAccountInput(
                private_key = ''
            )
        else:
            return CreateAccountInput(
        )
        """

    def testCreateAccountInput(self):
        """Test CreateAccountInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
