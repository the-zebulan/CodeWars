import unittest

from katas.kyu_4.snail import snail


class SnailTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(snail([
            [1, 2],
            [3, 4]
        ]), [1, 2, 4, 3])

    def test_equal_2(self):
        self.assertEqual(snail([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_equal_3(self):
        self.assertEqual(snail([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]), [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
