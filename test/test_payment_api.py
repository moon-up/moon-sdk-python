# coding: utf-8

"""
    moon-vault-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.payment_api import PaymentApi


class TestPaymentApi(unittest.TestCase):
    """PaymentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentApi()

    def tearDown(self) -> None:
        pass

    def test_moralis_webhook(self) -> None:
        """Test case for moralis_webhook

        """
        pass

    def test_payment_create_payment_intent(self) -> None:
        """Test case for payment_create_payment_intent

        """
        pass

    def test_payment_delete_payment_intent(self) -> None:
        """Test case for payment_delete_payment_intent

        """
        pass

    def test_payment_get_all_payment_intents(self) -> None:
        """Test case for payment_get_all_payment_intents

        """
        pass

    def test_payment_get_available_chains(self) -> None:
        """Test case for payment_get_available_chains

        """
        pass

    def test_payment_get_payment_intent(self) -> None:
        """Test case for payment_get_payment_intent

        """
        pass

    def test_payment_update_payment_intent(self) -> None:
        """Test case for payment_update_payment_intent

        """
        pass

    def test_tatum_webhook(self) -> None:
        """Test case for tatum_webhook

        """
        pass


if __name__ == '__main__':
    unittest.main()
