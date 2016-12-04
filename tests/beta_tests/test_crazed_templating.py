import unittest

from katas.beta.crazed_templating import letter_pattern


class LetterPatternTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(letter_pattern(['war', 'rad', 'dad']), "*a*")

    def test_equal_2(self):
        self.assertEqual(letter_pattern(
            ['general', 'admiral', 'piglets', 'secrets']), "*******")

    def test_equal_3(self):
        self.assertEqual(letter_pattern(['family']), "family")
