import unittest

from katas.beta.what_day_is_it import day


class DayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(day('20151208'), 'Tuesday')

    def test_equals_2(self):
        self.assertEqual(day('20140728'), 'Monday')

    def test_equals_3(self):
        self.assertEqual(day('20160229'), 'Monday')

    def test_equals_4(self):
        self.assertEqual(day('20160301'), 'Tuesday')

    def test_equals_5(self):
        self.assertEqual(day('19000228'), 'Wednesday')

    def test_equals_6(self):
        self.assertEqual(day('19000301'), 'Thursday')
