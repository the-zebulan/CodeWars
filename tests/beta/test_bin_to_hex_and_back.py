import unittest

from Beta.bin_to_hex_and_back import bin_to_hex, hex_to_bin


class BinaryHexTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bin_to_hex('000101'), '5')

    def test_equals_2(self):
        self.assertEqual(bin_to_hex('001111'), 'f')

    def test_equals_3(self):
        self.assertEqual(bin_to_hex('000'), '0')

    def test_equals_4(self):
        self.assertEqual(bin_to_hex('10011010010'), '4d2')

    def test_equals_5(self):
        self.assertEqual(hex_to_bin('0'), '0')

    def test_equals_6(self):
        self.assertEqual(hex_to_bin('f'), '1111')

    def test_equals_7(self):
        self.assertEqual(hex_to_bin('0F'), '1111')

    def test_equals_8(self):
        self.assertEqual(hex_to_bin('5'), '101')

    def test_equals_9(self):
        self.assertEqual(hex_to_bin('04D2'), '10011010010')

    def test_equals_10(self):
        self.assertEqual(hex_to_bin('A23'), '101000100011')


if __name__ == '__main__':
    unittest.main()
