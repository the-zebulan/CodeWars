import unittest

from katas.beta.algebraic_string import sum_prod


class SumsAndProductsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sum_prod("5*4+6"), '2.60000e+01')

    def test_equal_2(self):
        self.assertEqual(sum_prod("5+4*6"), '2.90000e+01')

    def test_equal_3(self):
        self.assertEqual(sum_prod("3*8+6*5"), '5.40000e+01')

    def test_equal_4(self):
        self.assertEqual(sum_prod("5*8+6*3*2"), '7.60000e+01')

    def test_equal_5(self):
        self.assertEqual(sum_prod("5.4*4.0+6.2+8.0"), '3.58000e+01')

    def test_equal_6(self):
        self.assertEqual(sum_prod("0.5*1.2*56+9.6*5*81+1"), '3.92260e+03')

    def test_equal_7(self):
        self.assertEqual(sum_prod("1"), '1.00000e+00')

    def test_equal_8(self):
        self.assertEqual(
            sum_prod("1.333333333*1.23456789+0.003*0.002"), '1.64610e+00'
        )
