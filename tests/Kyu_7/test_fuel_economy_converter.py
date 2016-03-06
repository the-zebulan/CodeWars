import unittest

from Kyu_7.fuel_economy_converter import lp100km2mpg, mpg2lp100km


class FuelEconomyConverterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(mpg2lp100km(42), 5.6)

    def test_equals_2(self):
        self.assertEqual(lp100km2mpg(9), 26.13)


if __name__ == '__main__':
    unittest.main()
