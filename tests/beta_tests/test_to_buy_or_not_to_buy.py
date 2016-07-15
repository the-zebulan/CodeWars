import unittest

from katas.beta.to_buy_or_not_to_buy import buy_or_pass


class BuyOrPassTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(buy_or_pass(800, 1000), 'Buy')

    def test_equals_2(self):
        self.assertEqual(buy_or_pass(12500.8, 15626), 'Buy')

    def test_equals_3(self):
        self.assertEqual(buy_or_pass(46.74, 58.43), 'Buy')

    def test_equals_4(self):
        self.assertEqual(buy_or_pass(56.74, 58.43), 'Pass')

    def test_equals_5(self):
        self.assertEqual(buy_or_pass(1000, 1000), 'Pass')
