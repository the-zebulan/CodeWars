import unittest

from katas.kyu_7.string_to_integer_conversion import my_parse_int


class StringToIntegerConversionTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(my_parse_int('1'), 1)

    def test_equals_2(self):
        self.assertEqual(my_parse_int('  1 '), 1)

    def test_equals_3(self):
        self.assertEqual(my_parse_int('08'), 8)

    def test_equals_4(self):
        self.assertEqual(my_parse_int('5 friends'), 'NaN')

    def test_equals_5(self):
        self.assertEqual(my_parse_int('16.5'), 'NaN')


if __name__ == '__main__':
    unittest.main()
