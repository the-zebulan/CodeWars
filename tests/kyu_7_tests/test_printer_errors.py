import unittest

from katas.kyu_7.printer_errors import printer_error


class PrinterErrorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(printer_error(
            'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'), '3/56'
        )

    def test_equals_2(self):
        self.assertEqual(printer_error('aaabbbbhaijjjm'), '0/14')

    def test_equals_3(self):
        self.assertEqual(printer_error('aaaxbbbbyyhwawiwjjjwwm'), '8/22')
