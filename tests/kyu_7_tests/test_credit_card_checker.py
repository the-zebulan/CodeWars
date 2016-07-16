import unittest

from katas.kyu_7.credit_card_checker import valid_card


class ValidCardTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(valid_card('5457 6238 9823 4311'))

    def test_true_2(self):
        self.assertTrue(valid_card('2222 2222 2222 2224'))

    def test_true_3(self):
        self.assertTrue(valid_card('9999 9999 9999 9995'))

    def test_true_4(self):
        self.assertTrue(valid_card('4444 4444 4444 4448'))

    def test_true_5(self):
        self.assertTrue(valid_card('3333 3333 3333 3331'))

    def test_true_6(self):
        self.assertTrue(valid_card('6666 6666 6666 6664'))

    def test_true_7(self):
        self.assertTrue(valid_card('0000 0000 0000 0000'))

    def test_true_8(self):
        self.assertTrue(valid_card('5457 6238 9823 4311'))

    def test_true_9(self):
        self.assertTrue(valid_card('8888 8888 8888 8888'))

    def test_true_10(self):
        self.assertTrue(valid_card('1111 1111 1111 1117'))

    def test_true_11(self):
        self.assertTrue(valid_card('1234 5678 9012 3452'))

    def test_true_12(self):
        self.assertTrue(valid_card('5555 5555 5555 5557'))

    def test_false_1(self):
        self.assertFalse(valid_card('8895 6238 9323 4311'))

    def test_false_2(self):
        self.assertFalse(valid_card('5457 6238 5568 4311'))

    def test_false_3(self):
        self.assertFalse(valid_card('5457 6238 9323 4311'))

    def test_false_4(self):
        self.assertFalse(valid_card('5457 1125 9323 4311'))

    def test_false_5(self):
        self.assertFalse(valid_card('1252 6238 9323 4311'))

    def test_false_6(self):
        self.assertFalse(valid_card('0000 0300 0000 0000'))

    def test_false_7(self):
        self.assertFalse(valid_card('5457 6238 9323 1252'))

    def test_false_8(self):
        self.assertFalse(valid_card('5457 6238 1251 4311'))

    def test_false_9(self):
        self.assertFalse(valid_card('5457 6238 0254 4311'))

    def test_false_10(self):
        self.assertFalse(valid_card('5457 1111 9323 4311'))

    def test_false_11(self):
        self.assertFalse(valid_card('1145 6238 9323 4311'))

    def test_false_12(self):
        self.assertFalse(valid_card('0025 2521 9323 4311'))

    def test_false_13(self):
        self.assertFalse(valid_card('5457 6238 9323 4311'))

    def test_false_14(self):
        self.assertFalse(valid_card('5458 4444 9323 4311'))

    def test_false_15(self):
        self.assertFalse(valid_card('5457 6238 3333 4311'))

    def test_false_16(self):
        self.assertFalse(valid_card('0123 4567 8901 2345'))
