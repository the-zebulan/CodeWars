import unittest

from katas.beta.caesar_cipher_encryption_variation import caesar_encode


class CaesarEncodeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(
            caesar_encode('conquer et impera', 130), 'conquer fu korgtc'
        )

    def test_equal_2(self):
        self.assertEqual(
            caesar_encode('fere libenter homines id quod volunt credunt', 70),
            'xwjw ebuxgmxk bigchym dy mqkz slirkq apcbslr'
        )

    def test_equal_3(self):
        self.assertEqual(
            caesar_encode('alea iacta est', 300), 'ozso xprip uij'
        )

    def test_equal_4(self):
        self.assertEqual(
            caesar_encode('horum omnium fortissimi sunt belgae', 0),
            'horum pnojvn hqtvkuukok vxqw fipkei'
        )
