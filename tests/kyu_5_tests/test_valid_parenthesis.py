import unittest

from katas.kyu_5.valid_parenthesis import valid_parentheses


class ValidParenthesisTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(valid_parentheses(""))

    def test_true_2(self):
        self.assertTrue(valid_parentheses("hi(hi)()"))

    def test_false_1(self):
        self.assertFalse(valid_parentheses("  ("))

    def test_false_2(self):
        self.assertFalse(valid_parentheses(")test"))

    def test_false_3(self):
        self.assertFalse(valid_parentheses("hi())("))


if __name__ == '__main__':
    unittest.main()
