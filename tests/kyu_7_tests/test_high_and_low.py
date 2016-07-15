import unittest

from katas.kyu_7.high_and_low import high_and_low


class HighAndLowTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(high_and_low('1 2 3 4 5'), '5 1')

    def test_equals_2(self):
        self.assertEqual(high_and_low('1 2 -3 4 5'), '5 -3')

    def test_equals_3(self):
        self.assertEqual(high_and_low('1 9 3 4 -5'), '9 -5')
