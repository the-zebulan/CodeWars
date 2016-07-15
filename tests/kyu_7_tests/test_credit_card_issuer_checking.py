import unittest

from katas.kyu_7.credit_card_issuer_checking import get_issuer


class GetIssuerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_issuer(4111111111111111), 'VISA')

    def test_equals_2(self):
        self.assertEqual(get_issuer(4111111111111), 'VISA')

    def test_equals_3(self):
        self.assertEqual(get_issuer(4012888888881881), 'VISA')

    def test_equals_4(self):
        self.assertEqual(get_issuer(378282246310005), 'AMEX')

    def test_equals_5(self):
        self.assertEqual(get_issuer(6011111111111117), 'Discover')

    def test_equals_6(self):
        self.assertEqual(get_issuer(5105105105105100), 'Mastercard')

    def test_equals_7(self):
        self.assertEqual(get_issuer(5105105105105106), 'Mastercard')

    def test_equals_8(self):
        self.assertEqual(get_issuer(9111111111111111), 'Unknown')
