import unittest

from katas.beta.simple_encryption_1_alternating_split import decrypt, encrypt


class AlternatingSplitTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(encrypt('This is a test!', 0), 'This is a test!')

    def test_equal_2(self):
        self.assertEqual(encrypt('This is a test!', 1), 'hsi  etTi sats!')

    def test_equal_3(self):
        self.assertEqual(encrypt('This is a test!', 2), 's eT ashi tist!')

    def test_equal_4(self):
        self.assertEqual(encrypt('This is a test!', 3), ' Tah itse sits!')

    def test_equal_5(self):
        self.assertEqual(encrypt('This is a test!', 4), 'This is a test!')

    def test_equal_6(self):
        self.assertEqual(encrypt('This is a test!', -1), 'This is a test!')

    def test_equal_7(self):
        self.assertEqual(encrypt('This kata is very interesting!', 1),
                         'hskt svr neetn!Ti aai eyitrsig')

    def test_equal_8(self):
        self.assertEqual(decrypt('This is a test!', 0), 'This is a test!')

    def test_equal_9(self):
        self.assertEqual(decrypt('hsi  etTi sats!', 1), 'This is a test!')

    def test_equal_10(self):
        self.assertEqual(decrypt('s eT ashi tist!', 2), 'This is a test!')

    def test_equal_11(self):
        self.assertEqual(decrypt(' Tah itse sits!', 3), 'This is a test!')

    def test_equal_12(self):
        self.assertEqual(decrypt('This is a test!', 4), 'This is a test!')

    def test_equal_13(self):
        self.assertEqual(decrypt('This is a test!', -1), 'This is a test!')

    def test_equal_14(self):
        self.assertEqual(decrypt('hskt svr neetn!Ti aai eyitrsig', 1),
                         'This kata is very interesting!')

    def test_equal_15(self):
        self.assertEqual(encrypt('', 0), '')

    def test_equal_16(self):
        self.assertEqual(decrypt('', 0), '')

    def test_is_none_1(self):
        self.assertIsNone(encrypt(None, 0))

    def test_is_none_2(self):
        self.assertIsNone(decrypt(None, 0))
