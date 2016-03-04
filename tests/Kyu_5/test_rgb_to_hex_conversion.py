import unittest

from Kyu_5.rgb_to_hex_conversion import rgb


class RGBToHexTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(rgb(0, 0, 0), '000000')

    def test_equals_2(self):
        self.assertEqual(rgb(1, 2, 3), '010203')

    def test_equals_3(self):
        self.assertEqual(rgb(-20, 275, 125), '00FF7D')

    def test_equals_4(self):
        self.assertEqual(rgb(148, 0, 211), '9400D3')

    def test_equals_5(self):
        self.assertEqual(rgb(254, 253, 252), 'FEFDFC')

    def test_equals_6(self):
        self.assertEqual(rgb(255, 255, 255), 'FFFFFF')

    def test_equals_7(self):
        self.assertEqual(rgb(255, 255, 300), 'FFFFFF')


if __name__ == '__main__':
    unittest.main()
