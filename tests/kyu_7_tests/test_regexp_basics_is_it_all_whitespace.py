import unittest

from katas.kyu_7.regexp_basics_is_it_all_whitespace import whitespace


class WhitespaceTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(whitespace(''))

    def test_true_2(self):
        self.assertTrue(whitespace(' '))

    def test_true_3(self):
        self.assertTrue(whitespace('\n\r\n\r'))

    def test_true_4(self):
        self.assertTrue(whitespace('\t'))

    def test_true_5(self):
        self.assertTrue(whitespace('\t \n\r\n  '))

    def test_true_6(self):
        self.assertTrue(whitespace('\n\r\n\r '))

    def test_false(self):
        self.assertFalse(whitespace('a'))

    def test_false_2(self):
        self.assertFalse(whitespace('w\n'))

    def test_false_3(self):
        self.assertFalse(whitespace(' a\n'))

    def test_false_4(self):
        self.assertFalse(whitespace('\n\r\n\r 3'))
