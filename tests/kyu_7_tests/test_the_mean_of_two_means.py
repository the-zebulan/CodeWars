import unittest

from katas.kyu_7.the_mean_of_two_means import get_mean


class GetMeanTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_mean([1, 3, 2, 4], 2, 3), 2.5)

    def test_equal_2(self):
        self.assertEqual(get_mean([1, 3, 2], 2, 2), 2.25)

    def test_equal_3(self):
        self.assertEqual(get_mean([1, 3, 2, 4], 1, 2), -1)

    def test_equal_4(self):
        self.assertEqual(get_mean([1, 3, 2, 4], 2, 8), -1)

    def test_equal_5(self):
        self.assertEqual(get_mean([1, -1, 2, -1], 2, 3), 0)
