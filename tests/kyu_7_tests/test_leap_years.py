import unittest

from katas.kyu_7.leap_years import isLeapYear


class IsLeapYearTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(isLeapYear(1984))

    def test_true_2(self):
        self.assertTrue(isLeapYear(2000))

    def test_false(self):
        self.assertFalse(isLeapYear(1234))

    def test_false_2(self):
        self.assertFalse(isLeapYear(1100))
