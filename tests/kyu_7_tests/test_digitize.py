import unittest

from katas.kyu_7.digitize import digitize


class DigitizeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(digitize(123), [1, 2, 3])

    def test_equals_2(self):
        self.assertEqual(digitize(1), [1])

    def test_equals_3(self):
        self.assertEqual(digitize(0), [0])

    def test_equals_4(self):
        self.assertEqual(digitize(1230), [1, 2, 3, 0])

    def test_equals_5(self):
        self.assertEqual(digitize(8675309), [8, 6, 7, 5, 3, 0, 9])
