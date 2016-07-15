import unittest

from katas.kyu_7.after_midnight import day_and_time


class DayAndTimeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(day_and_time(0), 'Sunday 00:00')

    def test_equals_2(self):
        self.assertEqual(day_and_time(-3), 'Saturday 23:57')

    def test_equals_3(self):
        self.assertEqual(day_and_time(45), 'Sunday 00:45')

    def test_equals_4(self):
        self.assertEqual(day_and_time(759), 'Sunday 12:39')

    def test_equals_5(self):
        self.assertEqual(day_and_time(1236), 'Sunday 20:36')

    def test_equals_6(self):
        self.assertEqual(day_and_time(1447), 'Monday 00:07')

    def test_equals_7(self):
        self.assertEqual(day_and_time(7832), 'Friday 10:32')

    def test_equals_8(self):
        self.assertEqual(day_and_time(18876), 'Saturday 02:36')

    def test_equals_9(self):
        self.assertEqual(day_and_time(259180), 'Thursday 23:40')

    def test_equals_10(self):
        self.assertEqual(day_and_time(-349000), 'Tuesday 15:20')
