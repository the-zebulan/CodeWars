import unittest

from katas.kyu_7.filter_unused_digits import unused_digits


class UnusedDigitsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(unused_digits(12, 34, 56, 78), '09')

    def test_equals_2(self):
        self.assertEqual(unused_digits(2015, 8, 26), '3479')

    def test_equals_3(self):
        self.assertEqual(unused_digits(276, 575), '013489')

    def test_equals_4(self):
        self.assertEqual(unused_digits(643), '0125789')

    def test_equals_5(self):
        self.assertEqual(unused_digits(864, 896, 744), '01235')
