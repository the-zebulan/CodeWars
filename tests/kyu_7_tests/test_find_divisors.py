import unittest

from katas.kyu_7.find_divisors import divisors


class DivisorsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(divisors(1), 1)

    def test_equals_2(self):
        self.assertEqual(divisors(4), 3)
