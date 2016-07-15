import unittest

from katas.kyu_7.integer_to_currency_format import to_currency


class IntegerToCurrencyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_currency(123456), '123,456')

    def test_equals_2(self):
        self.assertEqual(to_currency(1234), '1,234')

    def test_equals_3(self):
        self.assertEqual(to_currency(123), '123')

    def test_equals_4(self):
        self.assertEqual(to_currency(123456789012), '123,456,789,012')
