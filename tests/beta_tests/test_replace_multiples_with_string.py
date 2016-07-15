import unittest

from katas.beta.replace_multiples_with_string import getNumber, getNumberRange


class ReplaceMultiplesWithStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(getNumber(0), 'BOTH')

    def test_equals_2(self):
        self.assertEqual(getNumber(1), 1)

    def test_equals_3(self):
        self.assertEqual(getNumber(2), 2)

    def test_equals_4(self):
        self.assertEqual(getNumber(3), 'THREE')

    def test_equals_5(self):
        self.assertEqual(getNumber(4), 4)

    def test_equals_6(self):
        self.assertEqual(getNumber(5), 'FIVE')

    def test_equals_7(self):
        self.assertEqual(getNumber(10), 'FIVE')

    def test_equals_8(self):
        self.assertEqual(getNumber(15), 'BOTH')

    def test_equals_9(self):
        self.assertEqual(getNumber(18), 'THREE')

    def test_equals_10(self):
        self.assertEqual(getNumber(19), 19)

    def test_equals_11(self):
        self.assertEqual(getNumber(30), 'BOTH')

    def test_equals_12(self):
        self.assertEqual(getNumber(150), 'BOTH')

    def test_equals_13(self):
        self.assertEqual(getNumber(-1), -1)

    def test_equals_14(self):
        self.assertEqual(getNumber(-3), 'THREE')

    def test_equals_15(self):
        self.assertEqual(getNumber(-15), 'BOTH')

    def test_equals_16(self):
        self.assertEqual(getNumber(-50), 'FIVE')

    def test_equals_17(self):
        self.assertEqual(getNumberRange(1, 15), [
            1, 2, 'THREE', 4, 'FIVE', 'THREE', 7, 8, 'THREE', 'FIVE', 11,
            'THREE', 13, 14, 'BOTH'
        ])

    def test_equals_18(self):
        self.assertEqual(getNumberRange(1, -15), [
            1, 'BOTH', -1, -2, 'THREE', -4, 'FIVE', 'THREE', -7, -8,
            'THREE', 'FIVE', -11, 'THREE', -13, -14, 'BOTH'
        ])
