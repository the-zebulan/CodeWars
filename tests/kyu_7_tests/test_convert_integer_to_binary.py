import unittest

from katas.kyu_7.convert_integer_to_binary import to_binary


class IntegerToBinaryTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(to_binary(2), '10')

    def test_equal_2(self):
        self.assertEqual(to_binary(3), '11')

    def test_equal_3(self):
        self.assertEqual(to_binary(4), '100')

    def test_equal_4(self):
        self.assertEqual(to_binary(5), '101')

    def test_equal_5(self):
        self.assertEqual(to_binary(7), '111')

    def test_equal_6(self):
        self.assertEqual(to_binary(10), '1010')

    def test_equal_7(self):
        self.assertEqual(to_binary(-3), '11111111111111111111111111111101')

    def test_equal_8(self):
        self.assertEqual(to_binary(0), '0')

    def test_equal_9(self):
        self.assertEqual(to_binary(1000), '1111101000')

    def test_equal_10(self):
        self.assertEqual(to_binary(-15), '11111111111111111111111111110001')

    def test_equal_11(self):
        self.assertEqual(to_binary(-1000),
                         '11111111111111111111110000011000')

    def test_equal_12(self):
        self.assertEqual(to_binary(-999999),
                         '11111111111100001011110111000001')

    def test_equal_13(self):
        self.assertEqual(to_binary(999999), '11110100001000111111')
