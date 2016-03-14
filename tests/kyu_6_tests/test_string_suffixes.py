import unittest

from katas.kyu_6.string_suffixes import string_suffix


class StringSuffixTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(string_suffix('ababaa'), 11)

    def test_equals_2(self):
        self.assertEqual(string_suffix('abc'), 3)


if __name__ == '__main__':
    unittest.main()
