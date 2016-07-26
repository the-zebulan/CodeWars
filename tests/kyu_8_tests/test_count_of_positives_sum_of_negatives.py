import unittest

from katas.kyu_8.count_of_positives_sum_of_negatives import \
    count_positives_sum_negatives


class CountPositivesSumNegativesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(count_positives_sum_negatives(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
        ), [10, -65])

    def test_equal_2(self):
        self.assertEqual(count_positives_sum_negatives(
            [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
        ), [8, -50])

    def test_equal_3(self):
        self.assertEqual(count_positives_sum_negatives([1]), [1, 0])

    def test_equal_4(self):
        self.assertEqual(count_positives_sum_negatives([-1]), [0, -1])

    def test_equal_5(self):
        self.assertEqual(count_positives_sum_negatives(
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ), [0, 0])
