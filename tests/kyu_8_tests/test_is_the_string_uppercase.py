import unittest

from katas.kyu_8.is_the_string_uppercase import is_uppercase


class IsUpperCaseTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_uppercase('C'))

    def test_true_2(self):
        self.assertTrue(is_uppercase('HELLO I AM DONALD'))

    def test_false(self):
        self.assertFalse(is_uppercase('c'))

    def test_false_2(self):
        self.assertFalse(is_uppercase('hello I AM DONALD'))


if __name__ == '__main__':
    unittest.main()
