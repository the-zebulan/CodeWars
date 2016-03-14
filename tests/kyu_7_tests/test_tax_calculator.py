import unittest

from kyu_7.tax_calculator import tax_calculator


class TaxCalculatorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(tax_calculator(1), 0.1)

    def test_equals_2(self):
        self.assertEqual(tax_calculator(10), 1)

    def test_equals_3(self):
        self.assertEqual(tax_calculator(11), 1.07)

    def test_equals_4(self):
        self.assertEqual(tax_calculator(15), 1.35)

    def test_equals_5(self):
        self.assertEqual(tax_calculator(18), 1.56)

    def test_equals_6(self):
        self.assertEqual(tax_calculator(21), 1.75)

    def test_equals_7(self):
        self.assertEqual(tax_calculator(26), 2)

    def test_equals_8(self):
        self.assertEqual(tax_calculator(30), 2.2)

    def test_equals_9(self):
        self.assertEqual(tax_calculator(30.49), 2.21)

    def test_equals_10(self):
        self.assertEqual(tax_calculator(35), 2.35)

    def test_equals_11(self):
        self.assertEqual(tax_calculator(100), 4.3)

    def test_equals_12(self):
        self.assertEqual(tax_calculator(1000000), 30001.3)

    def test_equals_13(self):
        self.assertEqual(tax_calculator(0), 0)

    def test_equals_14(self):
        self.assertEqual(tax_calculator(-3), 0)

    def test_equals_15(self):
        self.assertEqual(tax_calculator(None), 0)

    def test_equals_16(self):
        self.assertEqual(tax_calculator('monkey'), 0)


if __name__ == '__main__':
    unittest.main()
