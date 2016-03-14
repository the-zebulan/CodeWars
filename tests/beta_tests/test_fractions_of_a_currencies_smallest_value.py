import unittest

from beta.fractions_of_a_currencies_smallest_value import PriceDisplayFraction


class PriceDisplayFractionTestCase(unittest.TestCase):
    def test_equals(self):
        pdf = PriceDisplayFraction(32)
        self.assertEqual(pdf.to_internal('123.45/0'), 12345)
        self.assertEqual(pdf.to_display(12345), '123.45/0')

    def test_equals_2(self):
        pdf = PriceDisplayFraction(16)
        self.assertEqual(pdf.to_internal('123.45/2'), 12345.125)
        self.assertEqual(pdf.to_display(12345.125), '123.45/2')


if __name__ == '__main__':
    unittest.main()
