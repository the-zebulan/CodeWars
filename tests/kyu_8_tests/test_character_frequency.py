import unittest

from katas.kyu_8.character_frequency import char_freq


class CharacterFrequencyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(char_freq('abc'), {'a': 1, 'b': 1, 'c': 1})

    def test_equals_2(self):
        self.assertEqual(char_freq('aaabbbccc'), {'a': 3, 'b': 3, 'c': 3})
