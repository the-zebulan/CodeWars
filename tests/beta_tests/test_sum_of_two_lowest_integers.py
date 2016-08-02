import unittest

from katas.beta.sum_of_two_lowest_integers import sum_two_smallest_numbers


class SumOfTwoLowestIntegersTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)

    def test_equal_2(self):
        self.assertEqual(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)

    def test_equal_3(self):
        self.assertEqual(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)

    def test_equal_4(self):
        self.assertEqual(sum_two_smallest_numbers([1, 8, 12, 18, -1]), 0)

    def test_equal_5(self):
        self.assertEqual(sum_two_smallest_numbers([-1, -1]), -2)
