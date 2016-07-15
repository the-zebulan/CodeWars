import unittest

from katas.kyu_6.playing_with_digits import dig_pow


class PlayingWithDigitsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(dig_pow(695, 2), 2)

    def test_equals_2(self):
        self.assertEqual(dig_pow(46288, 3), 51)

    def test_equals_3(self):
        self.assertEqual(dig_pow(89, 1), 1)

    def test_equals_4(self):
        self.assertEqual(dig_pow(92, 1), -1)
