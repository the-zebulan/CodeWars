import unittest

from kyu_8.stringy_strings import stringy


class StringyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(stringy(5), '10101')

    def test_equals_2(self):
        self.assertEqual(stringy(6), '101010')

    def test_equals_3(self):
        self.assertEqual(stringy(4), '1010')

    def test_equals_4(self):
        self.assertEqual(stringy(12), '101010101010')


if __name__ == '__main__':
    unittest.main()
