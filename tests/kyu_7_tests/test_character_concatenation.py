import unittest

from kyu_7.character_concatenation import char_concat


class CharacterConcatenationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(char_concat('abcdef'), 'af1be2cd3')

    def test_equals_2(self):
        self.assertEqual(char_concat('abc!def'), 'af1be2cd3')


if __name__ == '__main__':
    unittest.main()
