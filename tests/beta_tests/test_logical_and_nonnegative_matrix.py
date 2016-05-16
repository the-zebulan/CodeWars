import unittest

from katas.beta.logical_and_nonnegative_matrix import (
    logical_matrix, nonnegative_matrix, sum_nonnegative_logical_matrix)


class LogicalAndNonNegativeMatrixTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_nonnegative_logical_matrix(
            [[0, 0, 1], [1, 1, 0], [0, 0, 0]],
            [[0, 0, 1], [1, 1, 0], [0, 0, 0]]), 6)

    def test_true(self):
        self.assertTrue(logical_matrix([[0, 0], [1, 1]]))

    def test_true_2(self):
        self.assertTrue(nonnegative_matrix([[0, 0], [1, 1]]))

    def test_true_3(self):
        self.assertTrue(nonnegative_matrix([[0, 0, 0, 0], [1, 1, 0, 1]]))

    def test_false(self):
        self.assertFalse(logical_matrix([[2, 7], [0, 0]]))

    def test_false_2(self):
        self.assertFalse(logical_matrix([[1, 1], [1, 2]]))

    def test_false_3(self):
        self.assertFalse(sum_nonnegative_logical_matrix(
            [[-1, 0], [-1, 0]], [[0, -1], [0, -1]]
        ))


if __name__ == '__main__':
    unittest.main()
