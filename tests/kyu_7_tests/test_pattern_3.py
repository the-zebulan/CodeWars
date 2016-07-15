import unittest

from katas.kyu_7.pattern_3 import pattern


class PatternThreeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(1), '1')

    def test_equals_2(self):
        self.assertEqual(pattern(2), '2\n21')

    def test_equals_3(self):
        self.assertEqual(pattern(5), '5\n54\n543\n5432\n54321')
