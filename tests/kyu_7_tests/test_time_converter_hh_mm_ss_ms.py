import unittest
from datetime import datetime

from katas.kyu_7.time_converter_hh_mm_ss_ms import convert


class ConvertTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(convert(datetime(2016, 2, 8, 16, 42, 59)),
                         '16:42:59,000')

    def test_equals_2(self):
        self.assertEqual(convert(datetime(1951, 10, 31, 2, 2, 24, 399000)),
                         '02:02:24,399')

    def test_equals_3(self):
        self.assertEqual(convert(datetime(1523, 5, 29, 23, 2, 2, 9000)),
                         '23:02:02,009')

    def test_equals_4(self):
        self.assertEqual(convert(datetime(1, 1, 1, 1, 1, 1, 110000)),
                         '01:01:01,110')

    def test_equals_5(self):
        self.assertEqual(convert(datetime(9999, 9, 9, 9, 9, 9, 999999)),
                         '09:09:09,999')

    def test_equals_6(self):
        self.assertEqual(convert(datetime(2, 12, 30, 23, 59, 59, 875939)),
                         '23:59:59,875')

    def test_equals_7(self):
        self.assertEqual(convert(datetime(1850, 12, 30, 13, 39, 19)),
                         '13:39:19,000')

    def test_equals_8(self):
        self.assertEqual(convert(datetime(1978, 3, 18, 12, 0, 0, 0)),
                         '12:00:00,000')

    def test_equals_9(self):
        self.assertEqual(convert(datetime(1850, 12, 30, 11, 11, 11, 123939)),
                         '11:11:11,123')

    def test_equals_10(self):
        self.assertEqual(convert(datetime(1850, 12, 30, 0, 0, 0, 321939)),
                         '00:00:00,321')
