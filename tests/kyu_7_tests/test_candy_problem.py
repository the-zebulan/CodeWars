import unittest

from katas.kyu_7.candy_problem import candies


class CandiesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(candies([5, 8, 6, 4]), 9)

    def test_equal_2(self):
        self.assertEqual(candies([1, 2, 4, 6]), 11)

    def test_equal_3(self):
        self.assertEqual(candies([1, 6]), 5)

    def test_equal_4(self):
        self.assertEqual(candies([]), -1)

    def test_equal_5(self):
        self.assertEqual(candies([1, 2, None, 3]), -1)
