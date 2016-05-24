import unittest

from katas.beta.assignment_3 import keyword_cipher


class KeywordCipherTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(keyword_cipher('Welcome home', 'secret'),
                         'wticljt dljt')

    def test_equal_2(self):
        self.assertEqual(keyword_cipher('hello', 'wednesday'), 'bshhk')

    def test_equal_3(self):
        self.assertEqual(keyword_cipher('HELLO', 'wednesday'), 'bshhk')

    def test_equal_4(self):
        self.assertEqual(keyword_cipher('HeLlO', 'wednesday'), 'bshhk')

    def test_equal_5(self):
        self.assertEqual(keyword_cipher('WELCOME HOME', 'gridlocked'),
                         'wlfimhl kmhl')

    def test_equal_6(self):
        self.assertEqual(keyword_cipher('alpha bravo charlie', 'delta'),
                         'djofd eqdvn lfdqjga')

    def test_equal_7(self):
        self.assertEqual(keyword_cipher('Home Base', 'seven'), 'dlja esqa')

    def test_equal_8(self):
        self.assertEqual(keyword_cipher('basecamp', 'covert'), 'ocprvcil')

    def test_equal_9(self):
        self.assertEqual(keyword_cipher('one two three', 'rails'),
                         'mks twm tdpss')

    def test_equal_10(self):
        self.assertEqual(keyword_cipher('Test', 'unbuntu'), 'raqr')


if __name__ == '__main__':
    unittest.main()
