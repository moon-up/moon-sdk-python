# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.broadcast_input import BroadcastInput

class TestBroadcastInput(unittest.TestCase):
    """BroadcastInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BroadcastInput:
        """Test BroadcastInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BroadcastInput`
        """
        model = BroadcastInput()
        if include_optional:
            return BroadcastInput(
                chain_id = '',
                raw_transaction = ''
            )
        else:
            return BroadcastInput(
                chain_id = '',
                raw_transaction = '',
        )
        """

    def testBroadcastInput(self):
        """Test BroadcastInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
