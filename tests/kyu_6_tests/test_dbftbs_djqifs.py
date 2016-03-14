import unittest

from kyu_6.dbftbs_djqifs import encryptor


class EncryptorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(encryptor(13, ''), '')

    def test_equals_2(self):
        self.assertEqual(encryptor(13, 'Caesar Cipher'), 'Pnrfne Pvcure')

    def test_equals_3(self):
        self.assertEqual(encryptor(-5, 'Hello World!'), 'Czggj Rjmgy!')

    def test_equals_4(self):
        self.assertEqual(encryptor(27, 'Whoopi Goldberg'), 'Xippqj Hpmecfsh')


if __name__ == '__main__':
    unittest.main()
