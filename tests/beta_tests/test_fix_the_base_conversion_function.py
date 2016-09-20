import unittest

from katas.beta.fix_the_base_conversion_function import convert_num


class ConvertNumTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(convert_num(12463, ['num']), 'Invalid base input')

    def test_equal_2(self):
        self.assertEqual(convert_num(122, 'bin'), '0b1111010')

    def test_equal_3(self):
        self.assertEqual(convert_num('dog', 'bin'), 'Invalid number input')

    def test_equal_4(self):
        self.assertEqual(convert_num(0, 'hex'), '0x0')

    def test_equal_5(self):
        self.assertEqual(convert_num(123, 'lol'), 'Invalid base input')
