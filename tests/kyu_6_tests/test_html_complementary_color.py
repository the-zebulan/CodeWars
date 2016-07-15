import unittest

from katas.kyu_6.html_complementary_color import get_reversed_color


class ReversedColorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_reversed_color('01fD08'), '#FE02F7')

    def test_equals_2(self):
        self.assertEqual(get_reversed_color(''), '#FFFFFF')

    def test_equals_3(self):
        self.assertEqual(get_reversed_color('a23'), '#FFF5DC')

    def test_raises_1(self):
        self.assertRaises(ValueError, get_reversed_color, 123)

    def test_raises_2(self):
        self.assertRaises(ValueError, get_reversed_color, '#FFFFFFF')
