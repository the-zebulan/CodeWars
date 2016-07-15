import unittest

from katas.kyu_8.find_maximum_and_minimum_values_of_a_list import min, max


class MinMaxOfListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(min([-52, 56, 30, 29, -54, 0, -110]), -110)

    def test_equal_2(self):
        self.assertEqual(min([42, 54, 65, 87, 0]), 0)

    def test_equal_3(self):
        self.assertEqual(min([1, 2, 3, 4, 5, 10]), 1)

    def test_equal_4(self):
        self.assertEqual(min([-1, -2, -3, -4, -5, -10]), -10)

    def test_equal_5(self):
        self.assertEqual(min([9]), 9)

    def test_equal_6(self):
        self.assertEqual(max([-52, 56, 30, 29, -54, 0, -110]), 56)

    def test_equal_7(self):
        self.assertEqual(max([4, 6, 2, 1, 9, 63, -134, 566]), 566)

    def test_equal_8(self):
        self.assertEqual(max([5]), 5)

    def test_equal_9(self):
        self.assertEqual(
            max([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]), 555
        )

    def test_equal_10(self):
        self.assertEqual(max([9]), 9)
