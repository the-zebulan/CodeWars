import unittest

from katas.beta.this_is_odd import is_odd


class IsOddTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_odd(5))

    def test_true_2(self):
        self.assertTrue(is_odd(3.0))

    def test_true_3(self):
        self.assertTrue(is_odd(-1))

    def test_false(self):
        self.assertFalse(is_odd(4))
