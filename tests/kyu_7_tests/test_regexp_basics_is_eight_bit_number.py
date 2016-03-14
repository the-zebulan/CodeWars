import unittest

from katas.kyu_7.regexp_basics_is_eight_bit_number import \
    signed_eight_bit_number


class EightBitNumberTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(signed_eight_bit_number("0"))

    def test_true_2(self):
        self.assertTrue(signed_eight_bit_number("55"))

    def test_true_3(self):
        self.assertTrue(signed_eight_bit_number("-23"))

    def test_true_4(self):
        self.assertTrue(signed_eight_bit_number("127"))

    def test_true_5(self):
        self.assertTrue(signed_eight_bit_number("-128"))

    def test_false(self):
        self.assertFalse(signed_eight_bit_number(""))

    def test_false_2(self):
        self.assertFalse(signed_eight_bit_number("00"))

    def test_false_3(self):
        self.assertFalse(signed_eight_bit_number("-0"))

    def test_false_4(self):
        self.assertFalse(signed_eight_bit_number("042"))

    def test_false_5(self):
        self.assertFalse(signed_eight_bit_number("128"))

    def test_false_6(self):
        self.assertFalse(signed_eight_bit_number("999"))

    def test_false_7(self):
        self.assertFalse(signed_eight_bit_number("-129"))

    def test_false_8(self):
        self.assertFalse(signed_eight_bit_number("-999"))

    def test_false_9(self):
        self.assertFalse(signed_eight_bit_number("1\n"))

    def test_false_10(self):
        self.assertFalse(signed_eight_bit_number("1 "))

    def test_false_11(self):
        self.assertFalse(signed_eight_bit_number(" 1"))

    def test_false_12(self):
        self.assertFalse(signed_eight_bit_number("1\n2"))

    def test_false_13(self):
        self.assertFalse(signed_eight_bit_number("+1"))

    def test_false_14(self):
        self.assertFalse(signed_eight_bit_number("--1"))

    def test_false_15(self):
        self.assertFalse(signed_eight_bit_number("1\n"))

    def test_false_16(self):
        self.assertFalse(signed_eight_bit_number("1 "))

    def test_false_17(self):
        self.assertFalse(signed_eight_bit_number(" 1"))

    def test_false_18(self):
        self.assertFalse(signed_eight_bit_number("1\n2"))

    def test_false_19(self):
        self.assertFalse(signed_eight_bit_number("+1"))

    def test_false_20(self):
        self.assertFalse(signed_eight_bit_number("--1"))


if __name__ == '__main__':
    unittest.main()
