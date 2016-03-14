import unittest

from Kyu_7.string_chunks import string_chunk


class StringChunkTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(string_chunk('codewars', 2), ['co', 'de', 'wa', 'rs'])

    def test_equals_2(self):
        self.assertEqual(string_chunk('thiskataeasy', 4),
                         ['this', 'kata', 'easy'])

    def test_equals_3(self):
        self.assertEqual(string_chunk('hello world', 3),
                         ['hel', 'lo ', 'wor', 'ld'])

    def test_equals_4(self):
        self.assertEqual(string_chunk('everlong', 100), ['everlong'])


if __name__ == '__main__':
    unittest.main()
