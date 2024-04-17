# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from moonsdk.models.supported_payment_types_message import SupportedPaymentTypesMessage

class TestSupportedPaymentTypesMessage(unittest.TestCase):
    """SupportedPaymentTypesMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupportedPaymentTypesMessage:
        """Test SupportedPaymentTypesMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupportedPaymentTypesMessage`
        """
        model = SupportedPaymentTypesMessage()
        if include_optional:
            return SupportedPaymentTypesMessage(
                googlepay = moonsdk.models.payment_type.PaymentType(
                    icon = '', 
                    name = '', 
                    payment_type_id = '', ),
                applepay = moonsdk.models.payment_type.PaymentType(
                    icon = '', 
                    name = '', 
                    payment_type_id = '', ),
                creditcard = moonsdk.models.payment_type.PaymentType(
                    icon = '', 
                    name = '', 
                    payment_type_id = '', )
            )
        else:
            return SupportedPaymentTypesMessage(
                googlepay = moonsdk.models.payment_type.PaymentType(
                    icon = '', 
                    name = '', 
                    payment_type_id = '', ),
                applepay = moonsdk.models.payment_type.PaymentType(
                    icon = '', 
                    name = '', 
                    payment_type_id = '', ),
                creditcard = moonsdk.models.payment_type.PaymentType(
                    icon = '', 
                    name = '', 
                    payment_type_id = '', ),
        )
        """

    def testSupportedPaymentTypesMessage(self):
        """Test SupportedPaymentTypesMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
