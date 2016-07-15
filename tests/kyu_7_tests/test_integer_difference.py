import unittest

from katas.kyu_7.integer_difference import int_diff


class IntegerDifferenceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(int_diff([4, 8, 12, 12, 3, 6, 2], 6), 3)

    def test_equal_2(self):
        self.assertEqual(int_diff([1, 2, 3, 4, 5, 6, 7], 7), 0)

    def test_equal_3(self):
        self.assertEqual(int_diff([1, 6, 2, 3, 7, 8, 7], 0), 1)

    def test_equal_4(self):
        self.assertEqual(int_diff([1, 2, 3, 4], 0), 0)

    def test_equal_5(self):
        self.assertEqual(int_diff([1, 1, 1, 1], 0), 6)

    def test_equal_6(self):
        self.assertEqual(int_diff([], 3), 0)
