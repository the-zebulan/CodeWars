import unittest

from katas.kyu_8.convert_natural_num_to_binary import int_to_bin


class IntegerToBinaryTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(int_to_bin(0), '0')

    def test_equals_2(self):
        self.assertEqual(int_to_bin(8), '1000')

    def test_equals_3(self):
        self.assertEqual(int_to_bin(7), '111')
