import unittest

from katas.beta.vowel_shifting import vowel_shift


class VowelShiftTestCase(unittest.TestCase):
    def test_is_none_1(self):
        self.assertIsNone(vowel_shift(None, 0))

    def test_equal_1(self):
        self.assertEqual(vowel_shift('', 0), '')

    def test_equal_2(self):
        self.assertEqual(vowel_shift('This is a test!', 0), 'This is a test!')

    def test_equal_3(self):
        self.assertEqual(vowel_shift('This is a test!', 1), 'Thes is i tast!')

    def test_equal_4(self):
        self.assertEqual(vowel_shift('This is a test!', 3), 'This as e tist!')

    def test_equal_5(self):
        self.assertEqual(vowel_shift('This is a test!', 4), 'This is a test!')

    def test_equal_6(self):
        self.assertEqual(vowel_shift('This is a test!', -1), 'This as e tist!')

    def test_equal_7(self):
        self.assertEqual(vowel_shift('This is a test!', -5), 'This as e tist!')

    def test_equal_8(self):
        self.assertEqual(vowel_shift('Brrrr', 99), 'Brrrr')

    def test_equal_9(self):
        self.assertEqual(vowel_shift('AEIOUaeiou', 1), 'uAEIOUaeio')
