import unittest

from katas.beta.simple_encryption_2_index_difference import (
    VALID_CHARS, decrypt, encrypt
)


class IndexDifferenceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(encrypt('Business'), '&61kujla')

    def test_equal_2(self):
        self.assertEqual(decrypt('&61kujla'), 'Business')

    def test_equal_3(self):
        self.assertEqual(encrypt(
            "Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitemen"
            "t when finding a solution!"
        ), "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1V"
           "p2RV:wV9VuhO Iz3dqb.U0w")

    def test_equal_4(self):
        self.assertEqual(encrypt("This is a test!"), "5MyQa9p0riYplZc")

    def test_equal_5(self):
        self.assertEqual(encrypt("This kata is very interesting!"),
                         "5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p")

    def test_equal_6(self):
        self.assertEqual(decrypt(
            "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1"
            "Vp2RV:wV9VuhO Iz3dqb.U0w"
        ), "Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement"
           " when finding a solution!")

    def test_equal_7(self):
        self.assertEqual(decrypt("5MyQa9p0riYplZc"), "This is a test!")

    def test_equal_8(self):
        self.assertEqual(decrypt("5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p"),
                         "This kata is very interesting!")

    def test_equal_9(self):
        self.assertEqual(encrypt(""), "")

    def test_equal_10(self):
        self.assertEqual(decrypt(""), "")

    def test_equal_11(self):
        self.assertEqual(VALID_CHARS,
                         'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw'
                         'xyz0123456789.,:;-?! \'()$%&"')

    def test_is_none_1(self):
        self.assertIsNone(encrypt(None))

    def test_is_none_2(self):
        self.assertIsNone(decrypt(None))

    def test_raises_1(self):
        self.assertRaises(Exception, decrypt, '#+*/=<>@[]\\_^`{}|~')

    def test_raises_2(self):
        self.assertRaises(Exception, encrypt, '#+*/=<>@[]\\_^`{}|~')
