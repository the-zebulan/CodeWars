import unittest

from Kyu_7.formatting_decimal_places_1 import two_decimal_places


class TwoDecimalPlacesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(two_decimal_places(10.1289767789), 10.12)

    def test_equals_2(self):
        self.assertEqual(two_decimal_places(-7488.83485834983), -7488.83)

    def test_equals_3(self):
        self.assertEqual(two_decimal_places(4.653725356), 4.65)


if __name__ == '__main__':
    unittest.main()
