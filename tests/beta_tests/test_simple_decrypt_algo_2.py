import unittest

from katas.beta.simple_decrypt_algo_2 import decrypt


class DecryptTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(decrypt('$aaAA#bBb*Cc^Fff!z'),
                         '43200300000000000000000001')

    def test_equal_2(self):
        self.assertEqual(decrypt('z$AAA#ccc%EEE1234567890'),
                         '30303000000000000000000001')
