import unittest

from kyu_6.irreducible_sum_of_rationals import sum_fracts


class SumOfRationalsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12])

    def test_equals_2(self):
        self.assertEqual(sum_fracts([[1, 3], [5, 3]]), 2)


if __name__ == '__main__':
    unittest.main()
