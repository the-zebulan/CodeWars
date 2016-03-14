import unittest

from kyu_7.sexy_primes import sexy_prime


class SexyPrimeTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(sexy_prime(5, 11))

    def test_true_2(self):
        self.assertTrue(sexy_prime(13, 19))

    def test_true_3(self):
        self.assertTrue(sexy_prime(83, 89))

    def test_false(self):
        self.assertFalse(sexy_prime(1, 11))


if __name__ == '__main__':
    unittest.main()
