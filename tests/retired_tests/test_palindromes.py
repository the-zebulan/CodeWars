import unittest

from katas.retired.palindromes import is_palindrome


class IsPalindromeTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_palindrome(''))

    def test_true_2(self):
        self.assertTrue(is_palindrome('maoam'))

    def test_true_3(self):
        self.assertTrue(is_palindrome('If I had a hi-fi...'))

    def test_false(self):
        self.assertFalse(is_palindrome('abc'))
