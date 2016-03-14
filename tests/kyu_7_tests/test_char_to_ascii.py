import unittest

from Kyu_7.char_to_ascii import char_to_ascii


class CharToAsciiTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(char_to_ascii('a'), {'a': 97})

    def test_equals_2(self):
        self.assertEqual(char_to_ascii('aaa'), {'a': 97})

    def test_none(self):
        self.assertIsNone(char_to_ascii(''))


if __name__ == '__main__':
    unittest.main()
