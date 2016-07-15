import unittest

from katas.kyu_8.wilson_primes import am_i_wilson


class WilsonPrimesTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(am_i_wilson(5))

    def test_true_2(self):
        self.assertTrue(am_i_wilson(13))

    def test_true_3(self):
        self.assertTrue(am_i_wilson(563))

    def test_false(self):
        self.assertFalse(am_i_wilson(0))

    def test_false_2(self):
        self.assertFalse(am_i_wilson(1))

    def test_false_3(self):
        self.assertFalse(am_i_wilson(8))

    def test_false_4(self):
        self.assertFalse(am_i_wilson(9))
