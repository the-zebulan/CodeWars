import unittest

from katas.beta.circular_primes import circular_prime


class CircularPrimeTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(circular_prime(197))

    def test_true_2(self):
        self.assertTrue(circular_prime(971))

    def test_true_3(self):
        self.assertTrue(circular_prime(11939))

    def test_false(self):
        self.assertFalse(circular_prime(12345))

    def test_false_2(self):
        self.assertFalse(circular_prime(222))
