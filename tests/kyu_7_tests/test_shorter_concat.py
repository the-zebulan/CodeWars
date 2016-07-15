import unittest

from katas.kyu_7.shorter_concat import shorter_reverse_longer


class ShorterReverseLongerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(shorter_reverse_longer('first', 'abcde'),
                         'abcdetsrifabcde')

    def test_equals_2(self):
        self.assertEqual(shorter_reverse_longer('hello', 'bau'),
                         'bauollehbau')

    def test_equals_3(self):
        self.assertEqual(shorter_reverse_longer('abcde', 'fghi'),
                         'fghiedcbafghi')
