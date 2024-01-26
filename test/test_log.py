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

from moonsdk.models.log import Log

class TestLog(unittest.TestCase):
    """Log unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Log:
        """Test Log
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Log`
        """
        model = Log()
        if include_optional:
            return Log(
                triggers = [
                    moonsdk.models.trigger_output.TriggerOutput(
                        value = null, 
                        name = '', )
                    ],
                log_index = '',
                transaction_hash = '',
                address = '',
                data = '',
                topic0 = '',
                topic1 = '',
                topic2 = '',
                topic3 = ''
            )
        else:
            return Log(
                log_index = '',
                transaction_hash = '',
                address = '',
                data = '',
                topic0 = '',
                topic1 = '',
                topic2 = '',
                topic3 = '',
        )
        """

    def testLog(self):
        """Test Log"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
