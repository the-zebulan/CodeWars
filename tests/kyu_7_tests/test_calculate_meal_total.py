import unittest

from katas.kyu_7.calculate_meal_total import calculate_total


class CalculateTotalTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(calculate_total(5.00, 5, 10), 5.75)

    def test_equal_2(self):
        self.assertEqual(calculate_total(36.97, 7, 15), 45.10)

    def test_equal_3(self):
        self.assertEqual(calculate_total(0.00, 6, 18), 0.00)

    def test_equal_4(self):
        self.assertEqual(calculate_total(80.94, 0, 20), 97.13)

    def test_equal_5(self):
        self.assertEqual(calculate_total(54.96, 8, 0), 59.36)
