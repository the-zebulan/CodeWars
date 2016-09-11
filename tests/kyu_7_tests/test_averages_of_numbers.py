import unittest

from katas.kyu_7.averages_of_numbers import averages


class AveragesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(averages([2, 2, 2, 2, 2]), [2, 2, 2, 2])

    def test_equal_2(self):
        self.assertEqual(averages([2, -2, 2, -2, 2]), [0, 0, 0, 0])

    def test_equal_3(self):
        self.assertEqual(averages([1, 3, 5, 1, -10]), [2, 4, 3, -4.5])

    def test_equal_4(self):
        self.assertEqual(averages([]), [])
