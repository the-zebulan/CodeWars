import unittest

from katas.kyu_8.sum_mixed_array import sum_mix


class SumMixTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sum_mix([9, 3, '7', '3']), 22)

    def test_equal_2(self):
        self.assertEqual(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)

    def test_equal_3(self):
        self.assertEqual(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']), 41)

    def test_equal_4(self):
        self.assertEqual(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)

    def test_equal_5(self):
        self.assertEqual(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
