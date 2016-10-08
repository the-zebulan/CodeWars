import unittest

from katas.kyu_7.sentence_to_words import splitSentence


class SplitSentenceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(splitSentence('This string is splitsville'),
                         ['This', 'string', 'is', 'splitsville'])

    def test_equal_2(self):
        self.assertEqual(splitSentence('something'), ['something'])
