import unittest

from katas.kyu_7.beginner_series_sum_of_numbers import get_sum


class GetSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_sum(0, 1), 1)

    def test_equals_2(self):
        self.assertEqual(get_sum(0, -1), -1)


if __name__ == '__main__':
    unittest.main()
