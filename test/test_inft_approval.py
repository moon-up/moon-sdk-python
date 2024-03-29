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

from moonsdk.models.inft_approval import INFTApproval

class TestINFTApproval(unittest.TestCase):
    """INFTApproval unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> INFTApproval:
        """Test INFTApproval
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `INFTApproval`
        """
        model = INFTApproval()
        if include_optional:
            return INFTApproval(
                transaction_hash = '',
                contract = '',
                log_index = '',
                token_contract_type = '',
                token_name = '',
                token_symbol = '',
                account = '',
                operator = '',
                approved_all = True,
                token_id = ''
            )
        else:
            return INFTApproval(
                transaction_hash = '',
                contract = '',
                log_index = '',
                token_contract_type = '',
                token_name = '',
                token_symbol = '',
                account = '',
                operator = '',
                approved_all = True,
                token_id = '',
        )
        """

    def testINFTApproval(self):
        """Test INFTApproval"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
