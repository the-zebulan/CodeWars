import unittest

from katas.kyu_7.discover_the_original_price import discover_original_price


class DiscoverOriginalPriceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(discover_original_price(75, 25), 100)

    def test_equal_2(self):
        self.assertEqual(discover_original_price(25, 75), 100)

    def test_equal_3(self):
        self.assertEqual(discover_original_price(75.75, 25), 101)

    def test_equal_4(self):
        self.assertEqual(discover_original_price(373.85, 11.2), 421)

    def test_equal_5(self):
        self.assertEqual(discover_original_price(458.2, 17.13), 552.91)
