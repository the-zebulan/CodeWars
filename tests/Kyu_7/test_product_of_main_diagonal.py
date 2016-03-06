import unittest

from Kyu_7.product_of_main_diagonal import main_diagonal_product


class MainDiagonalProductTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(main_diagonal_product([[1, 0], [0, 1]]), 1)

    def test_equals_2(self):
        self.assertEqual(main_diagonal_product(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45
        )


if __name__ == '__main__':
    unittest.main()
