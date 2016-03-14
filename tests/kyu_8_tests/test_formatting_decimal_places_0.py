import unittest

from kyu_8.formatting_decimal_places_0 import two_decimal_places


class TwoDecimalPlacesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(two_decimal_places(4.659725356), 4.66)

    def test_equals_2(self):
        self.assertEqual(two_decimal_places(173735326.3783732637948948),
                         173735326.38)

    def test_equals_3(self):
        self.assertEqual(two_decimal_places(4.653725356), 4.65)


if __name__ == '__main__':
    unittest.main()
