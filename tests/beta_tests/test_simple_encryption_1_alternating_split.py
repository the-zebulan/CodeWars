import unittest

from katas.beta.simple_encryption_1_alternating_split import decrypt, encrypt


class AlternatingSplitTestCase(unittest.TestCase):
    def test_is_none_1(self):
        self.assertIsNone(encrypt(None, 0))

    def test_is_none_2(self):
        self.assertIsNone(decrypt(None, 0))

    def test_equal_1(self):
        self.assertEqual(encrypt('', 0), '')

    def test_equal_2(self):
        self.assertEqual(decrypt('', 0), '')

    def test_equal_3(self):
        self.assertEqual(encrypt('This is a test!', -1), 'This is a test!')

    def test_equal_4(self):
        self.assertEqual(encrypt("This is a another test!", 0), "This is a another test!")

    def test_equal_5(self):
        self.assertEqual(encrypt("This is a another test!", 1), "hsi  nte etTi saaohrts!")

    def test_equal_6(self):
        self.assertEqual(encrypt("This is a another test!", 2), "s neeT aorshi t tisaht!")

    def test_equal_7(self):
        self.assertEqual(encrypt("This is a another test!", 3), " eTarh  iatsne osittsh!")

    def test_equal_8(self):
        self.assertEqual(encrypt("This is a another test!", 4), "eah aseoith Tr itn sts!")

    def test_equal_9(self):
        self.assertEqual(encrypt("This is a another test!", 5), "a sot rinssehaeihT t t!")

    def test_equal_10(self):
        self.assertEqual(encrypt("This is a another test!", 6), " o iseaiTttastrnsheh  !")

    def test_equal_11(self):
        self.assertEqual(encrypt("This is a another test!", 7), "oieitatnhh   saTtsrse !")

    def test_equal_12(self):
        self.assertEqual(encrypt("This is a another test!", 8), "iianh sTss oetth  atre!")

    def test_equal_13(self):
        self.assertEqual(encrypt("This is a another test!", 9), "in Tsoth teiahss et ar!")

    def test_equal_14(self):
        self.assertEqual(encrypt("This is a another test!", 10), "nTohtihse ri st eas ta!")

    def test_equal_15(self):
        self.assertEqual(encrypt("This is a another test!", 11), "This is a another test!")

    def test_equal_16(self):
        self.assertEqual(encrypt("This is a another test!", 12), "hsi  nte etTi saaohrts!")

    def test_equal_17(self):
        self.assertEqual(encrypt("This is a another test!", 13), "s neeT aorshi t tisaht!")

    def test_equal_18(self):
        self.assertEqual(encrypt("This is a another test!", 14), " eTarh  iatsne osittsh!")

    def test_equal_19(self):
        self.assertEqual(encrypt("This is a another test!", 15), "eah aseoith Tr itn sts!")

    def test_equal_20(self):
        self.assertEqual(decrypt('This is a test!', -1), 'This is a test!')

    def test_equal_21(self):
        self.assertEqual(decrypt("This is a another test!", 0), "This is a another test!")

    def test_equal_22(self):
        self.assertEqual(decrypt("This is a another test!", 1), "nTohtihse ri st eas ta!")

    def test_equal_23(self):
        self.assertEqual(decrypt("This is a another test!", 2), "in Tsoth teiahss et ar!")

    def test_equal_24(self):
        self.assertEqual(decrypt("This is a another test!", 3), "iianh sTss oetth  atre!")

    def test_equal_25(self):
        self.assertEqual(decrypt("This is a another test!", 4), "oieitatnhh   saTtsrse !")

    def test_equal_26(self):
        self.assertEqual(decrypt("This is a another test!", 5), " o iseaiTttastrnsheh  !")

    def test_equal_27(self):
        self.assertEqual(decrypt("This is a another test!", 6), "a sot rinssehaeihT t t!")

    def test_equal_28(self):
        self.assertEqual(decrypt("This is a another test!", 7), "eah aseoith Tr itn sts!")

    def test_equal_29(self):
        self.assertEqual(decrypt("This is a another test!", 8), " eTarh  iatsne osittsh!")

    def test_equal_30(self):
        self.assertEqual(decrypt("This is a another test!", 9), "s neeT aorshi t tisaht!")

    def test_equal_31(self):
        self.assertEqual(decrypt("This is a another test!", 10), "hsi  nte etTi saaohrts!")

    def test_equal_32(self):
        self.assertEqual(decrypt("This is a another test!", 11), "This is a another test!")

    def test_equal_33(self):
        self.assertEqual(decrypt("This is a another test!", 12), "nTohtihse ri st eas ta!")

    def test_equal_34(self):
        self.assertEqual(decrypt("This is a another test!", 13), "in Tsoth teiahss et ar!")

    def test_equal_35(self):
        self.assertEqual(decrypt("This is a another test!", 14), "iianh sTss oetth  atre!")

    def test_equal_36(self):
        self.assertEqual(decrypt("This is a another test!", 15), "oieitatnhh   saTtsrse !")
