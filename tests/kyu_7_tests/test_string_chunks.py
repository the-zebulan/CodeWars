import unittest

from katas.kyu_7.string_chunks import string_chunk


class StringChunkTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(string_chunk('codewars', 2),
                         ['co', 'de', 'wa', 'rs'])

    def test_equal_2(self):
        self.assertEqual(string_chunk('thiskataeasy', 4),
                         ['this', 'kata', 'easy'])

    def test_equal_3(self):
        self.assertEqual(string_chunk('hello world', 3),
                         ['hel', 'lo ', 'wor', 'ld'])

    def test_equal_4(self):
        self.assertEqual(string_chunk('everlong', 100), ['everlong'])

    def test_equal_5(self):
        self.assertEqual(string_chunk(123), [])

    def test_equal_6(self):
        self.assertEqual(string_chunk('hello', 'z'), [])
