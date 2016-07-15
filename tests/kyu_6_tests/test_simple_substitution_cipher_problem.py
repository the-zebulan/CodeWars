import unittest

from katas.kyu_6.simple_substitution_cipher_helper import Cipher


class CipherTestCase(unittest.TestCase):
    def setUp(self):
        self.test1 = Cipher(
            'abcdefghijklmnopqrstuvwxyz', 'etaoinshrdlucmfwypvbgkjqxz')
        self.test2 = Cipher(
            'abcdefghijklmnopqrstuvwxyz', 'tfozcivbsjhengarudlkpwqxmy')

    def test_equals(self):
        self.assertEqual(self.test1.encode('abc'), 'eta')

    def test_equals_2(self):
        self.assertEqual(self.test1.encode('xyz'), 'qxz')

    def test_equals_3(self):
        self.assertEqual(self.test1.decode('eirfg'), 'aeiou')

    def test_equals_4(self):
        self.assertEqual(self.test1.decode('erlang'), 'aikcfu')

    def test_equals_5(self):
        self.assertEqual(self.test2.encode('abc'), 'tfo')

    def test_equals_6(self):
        self.assertEqual(self.test2.decode('tfo'), 'abc')

    def test_equals_7(self):
        self.assertEqual(self.test2.decode('kjpphi'), 'tjuukf')

    def test_equals_8(self):
        self.assertEqual(self.test2.encode('ajqqtb'), 'tjuukf')
