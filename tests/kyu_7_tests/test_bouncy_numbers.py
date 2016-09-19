import unittest

from katas.kyu_7.bouncy_numbers import is_bouncy


class IsBouncyTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(is_bouncy(101))

    def test_true_2(self):
        self.assertTrue(is_bouncy(120))

    def test_true_3(self):
        self.assertTrue(is_bouncy(2351))

    def test_false_1(self):
        self.assertFalse(is_bouncy(0))

    def test_false_2(self):
        self.assertFalse(is_bouncy(99))

    def test_false_3(self):
        self.assertFalse(is_bouncy(122))

    def test_false_4(self):
        self.assertFalse(is_bouncy(221))

    def test_false_5(self):
        self.assertFalse(is_bouncy(1235))

    def test_false_6(self):
        self.assertFalse(is_bouncy(5321))
