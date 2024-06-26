# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.supported_default_response_defaults import SupportedDefaultResponseDefaults

class TestSupportedDefaultResponseDefaults(unittest.TestCase):
    """SupportedDefaultResponseDefaults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupportedDefaultResponseDefaults:
        """Test SupportedDefaultResponseDefaults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupportedDefaultResponseDefaults`
        """
        model = SupportedDefaultResponseDefaults()
        if include_optional:
            return SupportedDefaultResponseDefaults(
                id = moonsdk.models.supported_default_response_defaults_id.SupportedDefaultResponse_defaults_id(
                    provider = '', 
                    payment_method = '', 
                    amount = 1.337, 
                    target = '', 
                    source = '', )
            )
        else:
            return SupportedDefaultResponseDefaults(
                id = moonsdk.models.supported_default_response_defaults_id.SupportedDefaultResponse_defaults_id(
                    provider = '', 
                    payment_method = '', 
                    amount = 1.337, 
                    target = '', 
                    source = '', ),
        )
        """

    def testSupportedDefaultResponseDefaults(self):
        """Test SupportedDefaultResponseDefaults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
