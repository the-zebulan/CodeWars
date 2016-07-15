import unittest

from katas.kyu_7.double_char import double_char


class DoubleCharTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(double_char('String'), 'SSttrriinngg')

    def test_equals_2(self):
        self.assertEqual(double_char('Hello World'), 'HHeelllloo  WWoorrlldd')

    def test_equals_3(self):
        self.assertEqual(double_char('1234!_ '), '11223344!!__  ')
