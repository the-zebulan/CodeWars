import unittest

from katas.kyu_6.character_frequency import letter_frequency


class LetterFrequencyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(letter_frequency('aaAabb dddDD hhcc'),
                         [('d', 5), ('a', 4), ('b', 2), ('c', 2), ('h', 2)])
