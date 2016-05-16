import unittest

from katas.kyu_7.filter_long_words import filter_long_words


class FilterLongWordsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(filter_long_words(
            'The quick brown fox jumps over the lazy dog', 4),
            ['quick', 'brown', 'jumps'])


if __name__ == '__main__':
    unittest.main()
