import unittest

from katas.kyu_6.good_vs_evil import goodVsEvil


class GoodVsEvilTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'),
                         'Battle Result: Evil eradicates all trace of Good')

    def test_equals_2(self):
        self.assertEqual(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'),
                         'Battle Result: Good triumphs over Evil')

    def test_equals_3(self):
        self.assertEqual(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'),
                         'Battle Result: No victor on this battle field')
