import unittest

from katas.kyu_7.sum_squares_of_numbers_in_list_that_may_contain_more_lists \
    import SumSquares


class SumSquaresTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(SumSquares([1, 2, 3]), 14)

    def test_equal_2(self):
        self.assertEqual(SumSquares([[1, 2], 3]), 14)

    def test_equal_3(self):
        self.assertEqual(SumSquares([[[[[[[[[1]]]]]]]]]), 1)

    def test_equal_4(self):
        self.assertEqual(SumSquares([10, [[10], 10], [10]]), 400)

    def test_equal_5(self):
        self.assertEqual(SumSquares(
            [1, [[3], 10, 5, [2, [3], [4], [5, [6]]]], [10]]
        ), 325)
