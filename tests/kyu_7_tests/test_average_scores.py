import unittest

from katas.kyu_7.average_scores import average


class AverageTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(average([5, 78, 52, 900, 1]), 207)

    def test_equal_2(self):
        self.assertEqual(average([5, 25, 50, 75]), 39)

    def test_equal_3(self):
        self.assertEqual(average([2]), 2)

    def test_equal_4(self):
        self.assertEqual(average([1, 1, 1, 1, 9999]), 2001)

    def test_equal_5(self):
        self.assertEqual(average([0]), 0)
