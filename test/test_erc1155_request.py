# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.erc1155_request import Erc1155Request

class TestErc1155Request(unittest.TestCase):
    """Erc1155Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Erc1155Request:
        """Test Erc1155Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Erc1155Request`
        """
        model = Erc1155Request()
        if include_optional:
            return Erc1155Request(
                to = '',
                data = '',
                input = '',
                value = '',
                nonce = '',
                gas = '',
                gas_price = '',
                chain_id = '',
                encoding = '',
                eoa = True,
                contract_address = '',
                token_id = '',
                token_ids = '',
                approved = True,
                broadcast = True
            )
        else:
            return Erc1155Request(
        )
        """

    def testErc1155Request(self):
        """Test Erc1155Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
