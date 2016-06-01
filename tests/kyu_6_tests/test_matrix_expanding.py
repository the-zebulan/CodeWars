import unittest

from katas.kyu_6.matrix_expanding import expand


class MatrixExpandingTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(expand([[1, 1], [1, 1]], 0),
                         [[0, 0, 0, 0],
                          [0, 1, 1, 0],
                          [0, 1, 1, 0],
                          [0, 0, 0, 0]])

    def test_equal_2(self):
        self.assertEqual(expand([[1, 1], [1, 1]], 'a'),
                         [['a', 'a', 'a', 'a'],
                          ['a', 1, 1, 'a'],
                          ['a', 1, 1, 'a'],
                          ['a', 'a', 'a', 'a']])

    def test_equal_3(self):
        self.assertEqual(expand([
            [1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]
        ], 'HI'), [['HI', 'HI', 'HI', 'HI', 'HI', 'HI', 'HI', 'HI'],
                   ['HI', 'HI', 'HI', 'HI', 'HI', 'HI', 'HI', 'HI'],
                   ['HI', 'HI', 1, 2, 3, 4, 'HI', 'HI'],
                   ['HI', 'HI', 5, 6, 7, 8, 'HI', 'HI'],
                   ['HI', 'HI', 9, 0, 1, 2, 'HI', 'HI'],
                   ['HI', 'HI', 3, 4, 5, 6, 'HI', 'HI'],
                   ['HI', 'HI', 'HI', 'HI', 'HI', 'HI', 'HI', 'HI'],
                   ['HI', 'HI', 'HI', 'HI', 'HI', 'HI', 'HI', 'HI']])


if __name__ == '__main__':
    unittest.main()
