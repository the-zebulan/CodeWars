import unittest

from katas.kyu_6.longest_2_character_substring import substring


class SubstringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(substring(''), '')

    def test_equals_2(self):
        self.assertEqual(substring('a'), 'a')

    def test_equals_3(self):
        self.assertEqual(substring('aa'), 'aa')

    def test_equals_4(self):
        self.assertEqual(substring('aaa'), 'aaa')

    def test_equals_5(self):
        self.assertEqual(substring('ab'), 'ab')

    def test_equals_6(self):
        self.assertEqual(substring('aba'), 'aba')

    def test_equals_7(self):
        self.assertEqual(substring('abc'), 'ab')

    def test_equals_8(self):
        self.assertEqual(substring('abacd'), 'aba')

    def test_equals_9(self):
        self.assertEqual(substring('abcba'), 'bcb')

    def test_equals_10(self):
        self.assertEqual(substring('bbacc'), 'bba')

    def test_equals_11(self):
        self.assertEqual(substring('ccddeeff'), 'ccdd')

    def test_equals_12(self):
        self.assertEqual(substring('abacddcd'), 'cddcd')

    def test_equals_13(self):
        self.assertEqual(substring('cefageaacceaccacca'), 'accacca')
