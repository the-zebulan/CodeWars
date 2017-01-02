import unittest

from katas.beta.simple_decrypt_algo import decrypt


class DecryptTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(decrypt('$aaaa#bbb*ccfff!z'),
                         '43200300000000000000000001')

    def test_equal_2(self):
        self.assertEqual(decrypt('z$aaa#ccc%eee1234567890'),
                         '30303000000000000000000001')
