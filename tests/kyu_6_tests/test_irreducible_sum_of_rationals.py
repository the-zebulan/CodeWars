import unittest

from katas.kyu_6.irreducible_sum_of_rationals import sum_fracts


class SumOfRationalsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12])

    def test_equal_2(self):
        self.assertEqual(sum_fracts([[1, 3], [5, 3]]), 2)

    def test_is_none_1(self):
        self.assertIsNone(sum_fracts([[0, 2], [0, 2]]))
