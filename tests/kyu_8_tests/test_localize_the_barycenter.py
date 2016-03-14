import unittest

from katas.kyu_8.localize_the_barycenter import bar_triang


class BarycenterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bar_triang(
            [4, 6], [12, 4], [10, 10]), [8.6667, 6.6667])

    def test_equals_2(self):
        self.assertEqual(bar_triang(
            [4, 2], [12, 2], [6, 10]), [7.3333, 4.6667])

    def test_equals_3(self):
        self.assertEqual(bar_triang(
            [4, 8], [8, 2], [16, 6]), [9.3333, 5.3333])


if __name__ == '__main__':
    unittest.main()
