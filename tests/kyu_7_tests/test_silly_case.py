import unittest

from katas.kyu_7.silly_case import sillycase


class SillyCaseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sillycase('foobar'), 'fooBAR')

    def test_equals_2(self):
        self.assertEqual(sillycase('codewars'), 'codeWARS')

    def test_equals_3(self):
        self.assertEqual(sillycase('brian'), 'briAN')
