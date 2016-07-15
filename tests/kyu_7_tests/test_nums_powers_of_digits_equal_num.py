import unittest

from katas.kyu_7.nums_powers_of_digits_equal_num import eq_sum_powdig


class PowersOfDigitsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(eq_sum_powdig(100, 2), [])

    def test_equals_2(self):
        self.assertEqual(eq_sum_powdig(1000, 2), [])

    def test_equals_3(self):
        self.assertEqual(eq_sum_powdig(200, 3), [153])

    def test_equals_4(self):
        self.assertEqual(eq_sum_powdig(370, 3), [153, 370])
