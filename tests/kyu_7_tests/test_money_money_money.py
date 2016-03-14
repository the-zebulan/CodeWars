import unittest

from katas.kyu_7.money_money_money import calculate_years


class CalculateYearsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(calculate_years(1000, 0.05, 0.18, 1100), 3)

    def test_equals_2(self):
        self.assertEqual(calculate_years(1000, 0.01625, 0.18, 1200), 14)

    def test_equals_3(self):
        self.assertEqual(calculate_years(1000, 0.05, .18, 1000), 0)


if __name__ == '__main__':
    unittest.main()
