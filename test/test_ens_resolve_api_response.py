# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.ens_resolve_api_response import EnsResolveAPIResponse

class TestEnsResolveAPIResponse(unittest.TestCase):
    """EnsResolveAPIResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnsResolveAPIResponse:
        """Test EnsResolveAPIResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnsResolveAPIResponse`
        """
        model = EnsResolveAPIResponse()
        if include_optional:
            return EnsResolveAPIResponse(
                success = True,
                message = '',
                body = moonsdk.models.input_body.InputBody(
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
                    broadcast = True, ),
                address = '',
                data = moonsdk.models.ens_resolve_response.EnsResolveResponse(
                    address = '', )
            )
        else:
            return EnsResolveAPIResponse(
                success = True,
                message = '',
        )
        """

    def testEnsResolveAPIResponse(self):
        """Test EnsResolveAPIResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
