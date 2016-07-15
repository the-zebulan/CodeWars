import unittest

from katas.beta.what_color_is_your_name import string_color


class StringColorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(string_color('Jack'), '79CAE5')

    def test_equals_2(self):
        self.assertEqual(string_color('Joshua'), '6A10D6')

    def test_equals_3(self):
        self.assertEqual(string_color('Joshua Smith'), '8F00FB')

    def test_equals_4(self):
        self.assertEqual(string_color('Hayden Smith'), '7E00EE')

    def test_equals_5(self):
        self.assertEqual(string_color('Mathew Smith'), '8B00F1')
