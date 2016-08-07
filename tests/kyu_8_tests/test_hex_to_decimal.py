import unittest

from katas.kyu_8.hex_to_decimal import hex_to_dec


class HexToDecimalTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(hex_to_dec("1"), 1)

    def test_equal_2(self):
        self.assertEqual(hex_to_dec("a"), 10)

    def test_equal_3(self):
        self.assertEqual(hex_to_dec("10"), 16)
