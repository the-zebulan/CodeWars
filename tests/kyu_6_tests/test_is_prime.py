import unittest

from katas.kyu_6.is_prime import is_prime


class IsPrimeTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_prime(2))

    def test_false(self):
        self.assertFalse(is_prime(0))

    def test_false_2(self):
        self.assertFalse(is_prime(1))

    def test_false_3(self):
        self.assertFalse(is_prime(4))
