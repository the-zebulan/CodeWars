import unittest

from katas.kyu_4.valid_braces import validBraces


class ValidBracesTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(validBraces('()'))

    def test_true_2(self):
        self.assertTrue(validBraces('[]'))

    def test_true_3(self):
        self.assertTrue(validBraces('{}'))

    def test_true_4(self):
        self.assertTrue(validBraces('{}()[]'))

    def test_true_5(self):
        self.assertTrue(validBraces('([{}])'))

    def test_true_6(self):
        self.assertTrue(validBraces('{}({})[]'))

    def test_true_7(self):
        self.assertTrue(validBraces('(({{[[]]}}))'))

    def test_false_1(self):
        self.assertFalse(validBraces('[(])'))

    def test_false_2(self):
        self.assertFalse(validBraces('(}'))

    def test_false_3(self):
        self.assertFalse(validBraces('([}{])'))

    def test_false_4(self):
        self.assertFalse(validBraces('(((({{'))

    def test_false_5(self):
        self.assertFalse(validBraces(')(}{]['))

    def test_false_6(self):
        self.assertFalse(validBraces('())({}}{()][]['))
