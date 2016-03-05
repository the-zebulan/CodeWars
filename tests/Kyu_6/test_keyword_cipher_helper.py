import unittest

from Kyu_6.keyword_cipher_helper import keyword_cipher


class KeywordCipherTestCase(unittest.TestCase):
    def setUp(self):
        self.cipher = keyword_cipher('abcdefghijklmnopqrstuvwxyz', 'keyword')

    def test_equals(self):
        self.assertEqual(self.cipher.encode('abc'), 'key')

    def test_equals_2(self):
        self.assertEqual(self.cipher.encode('xyz'), 'vxz')

    def test_equals_3(self):
        self.assertEqual(self.cipher.decode('key'), 'abc')

    def test_equals_4(self):
        self.assertEqual(self.cipher.decode('vxz'), 'xyz')


if __name__ == '__main__':
    unittest.main()
