import unittest

from katas.kyu_7.sorted_yes_no_how import is_sorted_and_how


class IsSortedAndHowTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(is_sorted_and_how([1, 2]), 'yes, ascending')

    def test_equal_2(self):
        self.assertEqual(is_sorted_and_how([1, 2, 3]), 'yes, ascending')

    def test_equal_3(self):
        self.assertEqual(is_sorted_and_how([3, 2, 1]), 'yes, descending')

    def test_equal_4(self):
        self.assertEqual(is_sorted_and_how([15, 7, 3, -8]), 'yes, descending')

    def test_equal_5(self):
        self.assertEqual(is_sorted_and_how([4, 2, 30]), 'no')

    def test_equal_6(self):
        self.assertEqual(is_sorted_and_how([3, 2, 4]), 'no')
