import unittest

from katas.kyu_7.invalid_input_error_handling_1 import get_count


class GetCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_count('Test'),
                         {'vowels': 1, 'consonants': 3})

    def test_equals_2(self):
        self.assertEqual(get_count('Here is some text'),
                         {'vowels': 6, 'consonants': 8})

    def test_equals_3(self):
        self.assertEqual(get_count('To be a Codewarrior or not to be'),
                         {'vowels': 12, 'consonants': 13})

    def test_equals_4(self):
        self.assertEqual(get_count('To Kata or not to Kata'),
                         {'vowels': 8, 'consonants': 9})

    def test_equals_5(self):
        self.assertEqual(get_count('aeiou'),
                         {'vowels': 5, 'consonants': 0})

    def test_equals_6(self):
        self.assertEqual(get_count('TEst'),
                         {'vowels': 1, 'consonants': 3})

    def test_equals_7(self):
        self.assertEqual(get_count('HEre Is sOme text'),
                         {'vowels': 6, 'consonants': 8})

    def test_equals_8(self):
        self.assertEqual(get_count(), {'vowels': 0, 'consonants': 0})

    def test_equals_9(self):
        self.assertEqual(get_count(['To Kata or not to Kata']),
                         {'vowels': 0, 'consonants': 0})

    def test_equals_10(self):
        self.assertEqual(get_count(None),
                         {'vowels': 0, 'consonants': 0})
