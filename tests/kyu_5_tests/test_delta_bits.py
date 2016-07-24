import unittest

from katas.kyu_5.delta_bits import convert_bits


class ConvertBitsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(convert_bits(31, 14), 2)

    def test_equal_2(self):
        self.assertEqual(convert_bits(7, 17), 3)

    def test_equal_3(self):
        self.assertEqual(convert_bits(31, 0), 5)

    def test_equal_4(self):
        self.assertEqual(convert_bits(0, 0), 0)

    def test_equal_5(self):
        self.assertEqual(convert_bits(127681, 127681), 0)

    def test_equal_6(self):
        self.assertEqual(convert_bits(312312312, 5645657), 13)

    def test_equal_7(self):
        self.assertEqual(convert_bits(43, 2009989843), 17)
