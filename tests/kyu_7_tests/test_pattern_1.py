import unittest

from katas.kyu_7.pattern_1 import pattern


class PatternOneTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(1), '1')

    def test_equals_2(self):
        self.assertEqual(pattern(2), '1\n22')

    def test_equals_3(self):
        self.assertEqual(pattern(5), '1\n22\n333\n4444\n55555')


if __name__ == '__main__':
    unittest.main()
