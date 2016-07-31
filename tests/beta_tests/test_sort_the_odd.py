import unittest

from katas.beta.sort_the_odd import sort_array


class SortTheOddTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sort_array([]), [])

    def test_equal_2(self):
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])

    def test_equal_3(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])

    def test_equal_4(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4, 11]),
                         [1, 3, 2, 8, 5, 4, 11])

    def test_equal_5(self):
        self.assertEqual(sort_array([2, 22, 37, 11, 4, 1, 5, 0]),
                         [2, 22, 1, 5, 4, 11, 37, 0])

    def test_equal_6(self):
        self.assertEqual(sort_array([1, 111, 11, 11, 2, 1, 5, 0]),
                         [1, 1, 5, 11, 2, 11, 111, 0])

    def test_equal_7(self):
        self.assertEqual(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    def test_equal_8(self):
        self.assertEqual(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_equal_9(self):
        self.assertEqual(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]),
                         [0, 1, 2, 3, 4, 5, 8, 7, 6, 9])
