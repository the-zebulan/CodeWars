import unittest

from katas.kyu_6.leap_year_with_restrictions import is_leap


class IsLeapTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(is_leap(1692))

    def test_true_2(self):
        self.assertTrue(is_leap(2000))

    def test_true_3(self):
        self.assertTrue(is_leap(2012))

    def test_false_1(self):
        self.assertFalse(is_leap(1731))

    def test_false_2(self):
        self.assertFalse(is_leap(1900))

    def test_false_3(self):
        self.assertFalse(is_leap(1987))

    def test_false_4(self):
        self.assertFalse(is_leap(2001))

    def test_false_5(self):
        self.assertFalse(is_leap(2014))

    def test_false_6(self):
        self.assertFalse(is_leap(2300))
