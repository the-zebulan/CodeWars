import unittest

from katas.kyu_6.rotation_cipher_cracker import decode


class DecodeTestCase(unittest.TestCase):
    def setUp(self):
        self.decoded_msgs = decode('lzwespnsdmwakafxafalq', 'max')

    def test_equals(self):
        self.assertEqual(decode('ymjxvznwwjqnxhzyj', 'squirrel'),
                         ['thesquirreliscute'])

    def test_equals_2(self):
        self.assertEqual(decode('lzwespnsdmwakafxafalq', 'max'),
                         ['maxftqotenxblbgybgbmr', 'themaxvalueisinfinity'])

    def test_in(self):
        self.assertIn('maxftqotenxblbgybgbmr', self.decoded_msgs)

    def test_in_2(self):
        self.assertIn('themaxvalueisinfinity', self.decoded_msgs)


if __name__ == '__main__':
    unittest.main()
