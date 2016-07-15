import unittest

from katas.kyu_6.word_patterns import word_pattern


class WordPatternTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(word_pattern('abab', 'apple banana apple banana'))

    def test_true_2(self):
        self.assertTrue(word_pattern('abba', 'car truck truck car'))

    def test_true_3(self):
        self.assertTrue(word_pattern('aaaa', 'cat cat cat cat'))

    def test_false(self):
        self.assertFalse(word_pattern('abab', 'apple banana banana apple'))

    def test_false_2(self):
        self.assertFalse(word_pattern('aaaa', 'cat cat dog cat'))
