import unittest

from katas.beta.bin_to_decimal import bin_to_decimal


class BinaryToDecimalTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(bin_to_decimal('1'), 1)

    def test_equal_2(self):
        self.assertEqual(bin_to_decimal('0'), 0)

    def test_equal_3(self):
        self.assertEqual(bin_to_decimal('1001001'), 73)
