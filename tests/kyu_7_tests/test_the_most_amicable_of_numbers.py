import unittest

from katas.kyu_7.the_most_amicable_of_numbers import amicable_numbers


class AmicableNumbersTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(amicable_numbers(220, 284))

    def test_true_2(self):
        self.assertTrue(amicable_numbers(1184, 1210))

    def test_true_3(self):
        self.assertTrue(amicable_numbers(10744, 10856))

    def test_true_4(self):
        self.assertTrue(amicable_numbers(122265, 139815))

    def test_true_5(self):
        self.assertTrue(amicable_numbers(220, 284))

    def test_true_6(self):
        self.assertTrue(amicable_numbers(220, 284))

    def test_false(self):
        self.assertFalse(amicable_numbers(220, 280))

    def test_false_2(self):
        self.assertFalse(amicable_numbers(220221, 282224))

    def test_false_3(self):
        self.assertFalse(amicable_numbers(299920, 9284))

    def test_false_4(self):
        self.assertFalse(amicable_numbers(999220, 2849))
