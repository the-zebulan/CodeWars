import unittest

from katas.kyu_6.cryptography_1_viva_cesare import caesar_crypto_encode


class CaesarCryptoEncodeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(caesar_crypto_encode('Et tu, Brute?', 3),
                         'Hw wx, Euxwh?')

    def test_equal_2(self):
        self.assertEqual(caesar_crypto_encode('Hw wx, Euxwh?', -3),
                         'Et tu, Brute?')

    def test_equal_3(self):
        self.assertEqual(caesar_crypto_encode('123,.)(!?', 10), '123,.)(!?')

    def test_equal_4(self):
        self.assertEqual(caesar_crypto_encode('', 10), '')

    def test_equal_5(self):
        self.assertEqual(caesar_crypto_encode(None, 10), '')

    def test_equal_6(self):
        self.assertEqual(caesar_crypto_encode('   ', 10), '')

    def test_equal_7(self):
        self.assertEqual(caesar_crypto_encode('Hello world!', 127),
                         'eBIIL TLOIA!')

    def test_equal_8(self):
        self.assertEqual(caesar_crypto_encode('eBIIL TLOIA!', -127),
                         'Hello world!')

    def test_equal_9(self):
        self.assertEqual(caesar_crypto_encode('ksdjai8983hdk?}{', 15),
                         'zHsypx8983wsz?}{')

    def test_equal_10(self):
        self.assertEqual(caesar_crypto_encode('Hello world!', 0),
                         'Hello world!')
