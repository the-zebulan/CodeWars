import unittest

from katas.kyu_7.convert_improper_fraction_to_mixed_numeral import \
    convert_to_mixed_numeral


class ConvertToMixedNumeralTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(convert_to_mixed_numeral('74/3'), '24 2/3')

    def test_equal_2(self):
        self.assertEqual(convert_to_mixed_numeral('9999/24'), '416 15/24')

    def test_equal_3(self):
        self.assertEqual(convert_to_mixed_numeral('74/30'), '2 14/30')

    def test_equal_4(self):
        self.assertEqual(convert_to_mixed_numeral('13/5'), '2 3/5')

    def test_equal_5(self):
        self.assertEqual(convert_to_mixed_numeral('5/3'), '1 2/3')

    def test_equal_6(self):
        self.assertEqual(convert_to_mixed_numeral('1/1'), '1')

    def test_equal_7(self):
        self.assertEqual(convert_to_mixed_numeral('10/10'), '1')

    def test_equal_8(self):
        self.assertEqual(convert_to_mixed_numeral('900/10'), '90')

    def test_equal_9(self):
        self.assertEqual(convert_to_mixed_numeral('9920/124'), '80')

    def test_equal_10(self):
        self.assertEqual(convert_to_mixed_numeral('6/2'), '3')

    def test_equal_11(self):
        self.assertEqual(convert_to_mixed_numeral('9/77'), '9/77')

    def test_equal_12(self):
        self.assertEqual(convert_to_mixed_numeral('96/100'), '96/100')

    def test_equal_13(self):
        self.assertEqual(convert_to_mixed_numeral('12/18'), '12/18')

    def test_equal_14(self):
        self.assertEqual(convert_to_mixed_numeral('6/36'), '6/36')

    def test_equal_15(self):
        self.assertEqual(convert_to_mixed_numeral('1/18'), '1/18')

    def test_equal_16(self):
        self.assertEqual(convert_to_mixed_numeral('-64/8'), '-8')

    def test_equal_17(self):
        self.assertEqual(convert_to_mixed_numeral('-6/8'), '-6/8')

    def test_equal_18(self):
        self.assertEqual(convert_to_mixed_numeral('-9/78'), '-9/78')

    def test_equal_19(self):
        self.assertEqual(convert_to_mixed_numeral('-504/26'), '-19 10/26')

    def test_equal_20(self):
        self.assertEqual(convert_to_mixed_numeral('-47/2'), '-23 1/2')

    def test_equal_21(self):
        self.assertEqual(convert_to_mixed_numeral('-21511/21'), '-1024 7/21')


if __name__ == '__main__':
    unittest.main()
