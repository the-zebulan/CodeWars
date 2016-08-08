import unittest

from katas.beta.sum_of_list_values import sum_list


class SumListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sum_list([]), 0)

    def test_equal_2(self):
        self.assertEqual(sum_list([1, 1]), 2)

    def test_equal_3(self):
        self.assertEqual(sum_list([2, 2]), 4)

    def test_equal_4(self):
        self.assertEqual(sum_list([2, 2, 2]), 6)

    def test_equal_5(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)
