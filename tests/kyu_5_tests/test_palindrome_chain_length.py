import unittest

from Kyu_5.palindrome_chain_length import palindrome_chain_length


class PalindromeChainLengthTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(palindrome_chain_length(87), 4)

    def test_equals_2(self):
        self.assertEqual(palindrome_chain_length(1), 0)

    def test_equals_3(self):
        self.assertEqual(palindrome_chain_length(88), 0)

    def test_equals_4(self):
        self.assertEqual(palindrome_chain_length(89), 24)

    def test_equals_5(self):
        self.assertEqual(palindrome_chain_length(10), 1)


if __name__ == '__main__':
    unittest.main()
