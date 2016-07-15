import unittest

from katas.kyu_6.regexp_basics_parsing_time import to_seconds


class ToSecondsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_seconds('00:00:00'), 0)

    def test_equals_2(self):
        self.assertEqual(to_seconds('01:02:03'), 3723)

    def test_equals_3(self):
        self.assertEqual(to_seconds('99:59:59'), 359999)

    def test_none_(self):
        self.assertIsNone(to_seconds('01:02:60'))

    def test_none_2(self):
        self.assertIsNone(to_seconds('01:60:03'))

    def test_none_3(self):
        self.assertIsNone(to_seconds('0:00:00'))

    def test_none_4(self):
        self.assertIsNone(to_seconds('00:0:00'))

    def test_none_5(self):
        self.assertIsNone(to_seconds('00:00:0'))

    def test_none_6(self):
        self.assertIsNone(to_seconds('00:00:00\n'))

    def test_none_7(self):
        self.assertIsNone(to_seconds('\n00:00:00'))
