import unittest

from katas.kyu_6.string_shortener_shrink import shorten


class ShortenTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(shorten(
            'The quick brown fox jumps over the lazy dog', 27
        ), 'The quick br...the lazy dog')

    def test_equal_2(self):
        self.assertEqual(shorten(
            'The quick brown fox jumps over the lazy dog', 27, '----'
        ), 'The quick b----the lazy dog')

    def test_equal_3(self):
        self.assertEqual(shorten('hello world', 5, '....'), 'hello')

    def test_equal_4(self):
        self.assertEqual(shorten('hello world', 6, '....'), 'h....d')

    def test_equal_5(self):
        self.assertEqual(shorten('hello', 7), 'hello')
