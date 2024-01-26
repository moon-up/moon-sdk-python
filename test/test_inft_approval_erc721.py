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

from moonsdk.models.inft_approval_erc721 import INFTApprovalERC721

class TestINFTApprovalERC721(unittest.TestCase):
    """INFTApprovalERC721 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> INFTApprovalERC721:
        """Test INFTApprovalERC721
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `INFTApprovalERC721`
        """
        model = INFTApprovalERC721()
        if include_optional:
            return INFTApprovalERC721(
                transaction_hash = '',
                contract = '',
                log_index = '',
                owner = '',
                approved = '',
                token_id = '',
                token_contract_type = '',
                token_name = '',
                token_symbol = ''
            )
        else:
            return INFTApprovalERC721(
                transaction_hash = '',
                contract = '',
                log_index = '',
                owner = '',
                approved = '',
                token_id = '',
                token_contract_type = '',
                token_name = '',
                token_symbol = '',
        )
        """

    def testINFTApprovalERC721(self):
        """Test INFTApprovalERC721"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
