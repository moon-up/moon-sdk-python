# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.get_supported_on_ramps_response_message_inner_icons_png import GetSupportedOnRampsResponseMessageInnerIconsPng

class TestGetSupportedOnRampsResponseMessageInnerIconsPng(unittest.TestCase):
    """GetSupportedOnRampsResponseMessageInnerIconsPng unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSupportedOnRampsResponseMessageInnerIconsPng:
        """Test GetSupportedOnRampsResponseMessageInnerIconsPng
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSupportedOnRampsResponseMessageInnerIconsPng`
        """
        model = GetSupportedOnRampsResponseMessageInnerIconsPng()
        if include_optional:
            return GetSupportedOnRampsResponseMessageInnerIconsPng(
                var_160x160 = '',
                var_32x32 = ''
            )
        else:
            return GetSupportedOnRampsResponseMessageInnerIconsPng(
                var_160x160 = '',
                var_32x32 = '',
        )
        """

    def testGetSupportedOnRampsResponseMessageInnerIconsPng(self):
        """Test GetSupportedOnRampsResponseMessageInnerIconsPng"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
