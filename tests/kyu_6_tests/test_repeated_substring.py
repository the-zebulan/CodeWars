import unittest

from katas.kyu_6.repeated_substring import f


class RepeatedSubstringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(f('ababab'), ('ab', 3))

    def test_equals_2(self):
        self.assertEqual(f('abcde'), ('abcde', 1))


if __name__ == '__main__':
    unittest.main()
