import unittest

from katas.kyu_7.operations_with_sets import process_2arrays


class ProcessTwoArraysTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(process_2arrays(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8, 10, 12, 14]
        ), [4, 8, 5, 3])

    def test_equals_2(self):
        self.assertEqual(process_2arrays(
            [33, 2, 3, 37, 38, 40, 12, 10, 43, 44, 47, 49, 8, 19, 22, 24,
             26, 28, 29, 30], [1, 34, 17, 7, 9, 10, 43, 49, 22, 27, 28]
        ), [5, 21, 15, 6])

    def test_equals_3(self):
        self.assertEqual(process_2arrays(
            [32, 34, 3, 4, 39, 10, 43, 13, 11, 18, 21, 22, 7, 25, 26, 36],
            [32, 5, 38, 8, 41, 42, 12, 48, 40, 21, 22, 26, 10, 30]
        ), [5, 20, 11, 9])

    def test_equals_4(self):
        self.assertEqual(process_2arrays(
            [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25],
            [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
        ), [3, 19, 9, 10])
