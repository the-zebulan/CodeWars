import unittest
from datetime import date

from katas.kyu_8.is_your_period_late import period_is_late


class PeriodIsLateTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(period_is_late(
            date(2016, 6, 13), date(2016, 7, 16), 28
        ))

    def test_true_2(self):
        self.assertTrue(period_is_late(
            date(2016, 7, 12), date(2016, 8, 10), 28
        ))

    def test_true_3(self):
        self.assertTrue(period_is_late(
            date(2016, 7, 1), date(2016, 8, 1), 30
        ))

    def test_true_4(self):
        self.assertTrue(period_is_late(
            date(2016, 1, 1), date(2016, 2, 1), 30
        ))

    def test_false_1(self):
        self.assertFalse(period_is_late(
            date(2016, 6, 13), date(2016, 7, 16), 35
        ))

    def test_false_2(self):
        self.assertFalse(period_is_late(
            date(2016, 6, 13), date(2016, 7, 16), 35
        ))

    def test_false_3(self):
        self.assertFalse(period_is_late(
            date(2016, 6, 13), date(2016, 6, 29), 28
        ))

    def test_false_4(self):
        self.assertFalse(period_is_late(
            date(2016, 7, 12), date(2016, 8, 9), 28
        ))

    def test_false_5(self):
        self.assertFalse(period_is_late(
            date(2016, 6, 1), date(2016, 6, 30), 30
        ))

    def test_false_6(self):
        self.assertFalse(period_is_late(
            date(2016, 1, 1), date(2016, 1, 31), 30
        ))
