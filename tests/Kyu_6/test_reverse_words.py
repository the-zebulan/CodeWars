import unittest

from Kyu_6.reverse_words import reverse_words


class ReverseWordsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(reverse_words(
            'The quick brown fox jumps over the lazy dog.'),
            'ehT kciuq nworb xof spmuj revo eht yzal .god')

    def test_equals_2(self):
        self.assertEqual(reverse_words('This is an example!'),
                         'sihT si na !elpmaxe')


if __name__ == '__main__':
    unittest.main()
