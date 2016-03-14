import unittest

from kyu_7.sum_first_nth_term_of_series import series_sum


class SeriesSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(series_sum(5), '1.57')

    def test_equals_2(self):
        self.assertEqual(series_sum(1), '1.00')

    def test_equals_3(self):
        self.assertEqual(series_sum(2), '1.25')

    def test_equals_4(self):
        self.assertEqual(series_sum(3), '1.39')


if __name__ == '__main__':
    unittest.main()
