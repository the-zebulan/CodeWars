import unittest

from katas.beta.time_for_validation import convert_time


class ConvertTimeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(convert_time('24', '09:00AM'), '09:00')

    def test_equals_2(self):
        self.assertEqual(convert_time('24', '09:00PM'), '21:00')

    def test_equals_3(self):
        self.assertEqual(convert_time('12', '08:13AM'), '08:13AM')

    def test_equals_4(self):
        self.assertEqual(convert_time('12', '05:19PM'), '05:19PM')

    def test_equals_5(self):
        self.assertEqual(convert_time('12', '21:13'), '09:13PM')

    def test_equals_6(self):
        self.assertEqual(convert_time('24', '22:33'), '22:33')

    def test_false_1(self):
        self.assertFalse(convert_time('99', '01:23AM'))

    def test_false_2(self):
        self.assertFalse(convert_time(99, '01:23AM'))

    def test_false_3(self):
        self.assertFalse(convert_time('12', '99:88PM'))
