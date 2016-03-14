import unittest

from Kyu_5.ascii_hex_converter import Converter


class ConverterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Converter.to_hex('Look mom, no hands'),
                         '4c6f6f6b206d6f6d2c206e6f2068616e6473')

    def test_equals_2(self):
        self.assertEqual(Converter.to_ascii(
            '4c6f6f6b206d6f6d2c206e6f2068616e6473'), 'Look mom, no hands')


if __name__ == '__main__':
    unittest.main()
