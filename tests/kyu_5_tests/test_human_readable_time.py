import unittest

from katas.kyu_5.human_readable_time import make_readable


class HumanReadableTimeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(make_readable(0), '00:00:00')

    def test_equals_2(self):
        self.assertEqual(make_readable(5), '00:00:05')

    def test_equals_3(self):
        self.assertEqual(make_readable(60), '00:01:00')

    def test_equals_4(self):
        self.assertEqual(make_readable(86399), '23:59:59')

    def test_equals_5(self):
        self.assertEqual(make_readable(359999), '99:59:59')
