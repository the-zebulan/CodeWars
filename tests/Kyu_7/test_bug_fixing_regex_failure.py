import unittest

from Kyu_7.bug_fixing_regex_failure import filter_words


class FilterWordsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(filter_words('You\'re Bad! timmy!'),
                         'You\'re awesome! timmy!')

    def test_equals_2(self):
        self.assertEqual(filter_words('You\'re MEAN! timmy!'),
                         'You\'re awesome! timmy!')


if __name__ == '__main__':
    unittest.main()
