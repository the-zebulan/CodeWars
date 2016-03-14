import unittest

from katas.kyu_5.metric_units_1 import meters


class MetersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(meters(5), '5m')

    def test_equals_2(self):
        self.assertEqual(meters(51500), '51.5km')

    def test_equals_3(self):
        self.assertEqual(meters(5000000), '5Mm')

    def test_equals_4(self):
        self.assertEqual(meters(999), '999m')

    def test_equals_5(self):
        self.assertEqual(meters(123456), '123.456km')

    def test_equals_6(self):
        self.assertEqual(meters(600), '600m')

    def test_equals_7(self):
        self.assertEqual(meters(9e+24), '9Ym')

    def test_equals_8(self):
        self.assertEqual(meters(400000000000000000000000), '400Zm')

    def test_equals_9(self):
        self.assertEqual(meters(7000000000000000000000000), '7Ym')

    def test_equals_10(self):
        self.assertEqual(meters(9000000000.0), '9Gm')


if __name__ == '__main__':
    unittest.main()
