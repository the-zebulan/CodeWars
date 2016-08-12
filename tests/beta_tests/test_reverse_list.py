import unittest

from katas.beta.reverse_list import reverse_list


class ReverseListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(reverse_list([]), [])

    def test_equal_2(self):
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_equal_3(self):
        self.assertEqual(reverse_list([2, 4, 5, 6]), [6, 5, 4, 2])
