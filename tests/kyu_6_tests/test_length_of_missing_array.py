import unittest

from katas.kyu_6.length_of_missing_array import get_length_of_missing_array


class LengthOfMissingArrayTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_length_of_missing_array(
            [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]
        ), 3)

    def test_equal_2(self):
        self.assertEqual(get_length_of_missing_array(
            [[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]
        ), 2)

    def test_equal_3(self):
        self.assertEqual(get_length_of_missing_array(
            [[None], [None, None, None]]
        ), 2)

    def test_equal_4(self):
        self.assertEqual(get_length_of_missing_array(
            [['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'],
             ['a', 'a', 'a', 'a', 'a', 'a']]
        ), 5)
