import unittest

from katas.beta.what_color_is_your_name import string_color


class StringColorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(string_color('Jack'), '7A90E5')

    def test_equals_2(self):
        self.assertEqual(string_color('Joshua'), '6C0FD7')

    def test_equals_3(self):
        self.assertEqual(string_color('Joshua Smith'), '935AFE')

    def test_equals_4(self):
        self.assertEqual(string_color('Hayden Smith'), '82F0F1')

    def test_equals_5(self):
        self.assertEqual(string_color('Mathew Smith'), '8F00F4')


if __name__ == '__main__':
    unittest.main()
