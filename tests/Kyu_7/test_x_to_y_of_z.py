import unittest

from Kyu_7.x_to_y_of_z import pagination_text


class PaginationTextTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pagination_text(1, 10, 30),
                         'Showing 1 to 10 of 30 Products.')

    def test_equals_2(self):
        self.assertEqual(pagination_text(3, 10, 26),
                         'Showing 21 to 26 of 26 Products.')

    def test_equals_3(self):
        self.assertEqual(pagination_text(1, 10, 8),
                         'Showing 1 to 8 of 8 Products.')

    def test_equals_4(self):
        self.assertEqual(pagination_text(2, 30, 350),
                         'Showing 31 to 60 of 350 Products.')

    def test_equals_5(self):
        self.assertEqual(pagination_text(1, 23, 30),
                         'Showing 1 to 23 of 30 Products.')

    def test_equals_6(self):
        self.assertEqual(pagination_text(2, 23, 30),
                         'Showing 24 to 30 of 30 Products.')

    def test_equals_7(self):
        self.assertEqual(pagination_text(43, 15, 3456),
                         'Showing 631 to 645 of 3456 Products.')


if __name__ == '__main__':
    unittest.main()
