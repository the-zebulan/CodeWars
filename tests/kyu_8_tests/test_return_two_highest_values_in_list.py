import unittest

from katas.kyu_8.return_two_highest_values_in_list import two_highest


class TwoHighestTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(two_highest([15, 20, 20, 17]), [20, 17])

    def test_equal_2(self):
        self.assertEqual(two_highest([43, 1, 2, 88]), [88, 43])

    def test_equal_3(self):
        self.assertEqual(two_highest([]), [])

    def test_false_1(self):
        self.assertFalse(two_highest('testing'))
