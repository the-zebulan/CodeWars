import unittest

from katas.kyu_8.sum_without_highest_and_lowest_number import sum_array


class SumArrayTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sum_array(None), 0)

    def test_equal_2(self):
        self.assertEqual(sum_array([]), 0)

    def test_equal_3(self):
        self.assertEqual(sum_array([3]), 0)

    def test_equal_4(self):
        self.assertEqual(sum_array([-3]), 0)

    def test_equal_5(self):
        self.assertEqual(sum_array([3, 5]), 0)

    def test_equal_6(self):
        self.assertEqual(sum_array([-3, -5]), 0)

    def test_equal_7(self):
        self.assertEqual(sum_array([6, 2, 1, 8, 10]), 16)

    def test_equal_8(self):
        self.assertEqual(sum_array([6, 0, 1, 10, 10]), 17)

    def test_equal_9(self):
        self.assertEqual(sum_array([-6, -20, -1, -10, -12]), -28)

    def test_equal_10(self):
        self.assertEqual(sum_array([-6, 20, -1, 10, -12]), 3)
