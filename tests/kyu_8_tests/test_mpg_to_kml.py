import unittest

from katas.kyu_8.mpg_to_kml import converter


class ConverterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(converter(12), 4.25)

    def test_equals_2(self):
        self.assertEqual(converter(24), 8.50)

    def test_equals_3(self):
        self.assertEqual(converter(36), 12.74)


if __name__ == '__main__':
    unittest.main()
