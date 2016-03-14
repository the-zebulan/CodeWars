import unittest

from beta.simple_barcode_scanner import barcode_scanner


class BarcodeScannerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(barcode_scanner(
            '1010111011011011100010110001011010111101101110101011100101110010'
            '1110010111001011011001000010101'), '789968000023')


if __name__ == '__main__':
    unittest.main()
