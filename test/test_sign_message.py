# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.sign_message import SignMessage

class TestSignMessage(unittest.TestCase):
    """SignMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignMessage:
        """Test SignMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignMessage`
        """
        model = SignMessage()
        if include_optional:
            return SignMessage(
                name = '',
                data = '',
                encoding = '',
                header = True,
                signtype = True
            )
        else:
            return SignMessage(
                data = '',
        )
        """

    def testSignMessage(self):
        """Test SignMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
