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

from moonsdk.models.transaction_input_supported_params_theme import TransactionInputSupportedParamsTheme

class TestTransactionInputSupportedParamsTheme(unittest.TestCase):
    """TransactionInputSupportedParamsTheme unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionInputSupportedParamsTheme:
        """Test TransactionInputSupportedParamsTheme
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionInputSupportedParamsTheme`
        """
        model = TransactionInputSupportedParamsTheme()
        if include_optional:
            return TransactionInputSupportedParamsTheme(
                border_radius = 1.337,
                card_color = '',
                secondary_text_color = '',
                primary_text_color = '',
                secondary_color = '',
                primary_color = '',
                theme_name = '',
                is_dark = True
            )
        else:
            return TransactionInputSupportedParamsTheme(
                border_radius = 1.337,
                card_color = '',
                secondary_text_color = '',
                primary_text_color = '',
                secondary_color = '',
                primary_color = '',
                theme_name = '',
                is_dark = True,
        )
        """

    def testTransactionInputSupportedParamsTheme(self):
        """Test TransactionInputSupportedParamsTheme"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
