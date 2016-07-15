import unittest

from katas.beta.swap_row_in_certain_columns_of_a_matrix import swap


class SwapTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(swap([[0, 1], [2, 3]], 0, 1, 0), [[2, 1], [0, 3]])

    def test_equal_2(self):
        self.assertEqual(swap([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2, 0, 2),
                         [[1, 2, 3], [7, 5, 9], [4, 8, 6]])

    def test_equal_3(self):
        self.assertEqual(swap([
            [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]
            ], 4, 2, 0, 2, 4
        ), [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [21, 12, 23, 14, 25],
            [16, 17, 18, 19, 20], [11, 22, 13, 24, 15], [26, 27, 28, 29, 30]])

    def test_equal_4(self):
        self.assertEqual(swap([
            ['m', 'a', 't', 'r', 'i'], ['x', 's', 'w', 'a', 'p']],
            0, 1, 0, 1, 3, 4
        ), [['x', 's', 't', 'a', 'p'], ['m', 'a', 'w', 'r', 'i']])

    def test_equal_5(self):
        self.assertEqual(swap([
            [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]
        ], 1, 3, 1, 3
        ), [[1, 5, 9, 13], [2, 8, 10, 16], [3, 7, 11, 15], [4, 6, 12, 14]])
