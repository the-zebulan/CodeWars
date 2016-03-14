import unittest

from katas.kyu_6.reversed_words import reverseWords


class ReverseWordsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(reverseWords(
            'The greatest victory is that which requires no battle'),
            'battle no requires which that is victory greatest The')

    def test_equals_2(self):
        self.assertEqual(reverseWords('hello world!'), 'world! hello')


if __name__ == '__main__':
    unittest.main()
