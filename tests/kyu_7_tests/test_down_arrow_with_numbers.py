import unittest

from katas.kyu_7.down_arrow_with_numbers import get_a_down_arrow_of


class DownArrowTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_a_down_arrow_of(10),
                         '1234567890987654321\n 12345678987654321\n  1234567'
                         '87654321\n   1234567654321\n    12345654321\n     '
                         '123454321\n      1234321\n       12321\n        12'
                         '1\n         1')

    def test_equals_2(self):
        self.assertEqual(get_a_down_arrow_of(0), '')

    def test_equals_3(self):
        self.assertEqual(get_a_down_arrow_of(-5), '')

    def test_equals_4(self):
        self.assertEqual(get_a_down_arrow_of(3), '12321\n 121\n  1')

    def test_equals_5(self):
        self.assertEqual(get_a_down_arrow_of(5),
                         '123454321\n 1234321\n  12321\n   121\n    1')
