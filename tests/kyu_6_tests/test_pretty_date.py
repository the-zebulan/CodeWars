import unittest

from katas.kyu_6.pretty_date import to_pretty


class PrettyDateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_pretty(300), '5 minutes ago')

    def test_equals_2(self):
        self.assertEqual(to_pretty(60), 'a minute ago')

    def test_equals_3(self):
        self.assertEqual(to_pretty(3600), 'an hour ago')
