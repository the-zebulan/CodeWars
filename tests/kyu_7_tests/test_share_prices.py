import unittest

from katas.kyu_7.share_prices import share_price


class SharePriceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(share_price(100, []), '100.00')

    def test_equals_2(self):
        self.assertEqual(share_price(100, [-50, 50]), '75.00')

    def test_equals_3(self):
        self.assertEqual(share_price(100, [-50, 100]), '100.00')

    def test_equals_4(self):
        self.assertEqual(share_price(100, [-20, 30]), '104.00')

    def test_equals_5(self):
        self.assertEqual(share_price(1000, [0, 2, 3, 6]), '1113.64')


if __name__ == '__main__':
    unittest.main()
