import unittest

from katas.beta.palindrome_checker import is_palindrome


class IsPalindromeTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_palindrome('race car'))

    def test_true_2(self):
        self.assertTrue(is_palindrome('Amor, Roma'))

    def test_true_3(self):
        self.assertTrue(is_palindrome('No \'x\' in Nixon'))

    def test_false(self):
        self.assertFalse(is_palindrome(None))

    def test_false_2(self):
        self.assertFalse(is_palindrome('aaaaza'))


if __name__ == '__main__':
    unittest.main()
