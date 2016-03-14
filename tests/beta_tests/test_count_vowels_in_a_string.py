import unittest

from katas.beta.count_vowels_in_a_string import count_vowels


class CountVowelsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count_vowels('abcdefg'), 2)

    def test_equals_2(self):
        self.assertEqual(count_vowels('asdfdsafdsafds'), 3)


if __name__ == '__main__':
    unittest.main()
