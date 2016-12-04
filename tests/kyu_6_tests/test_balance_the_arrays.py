import unittest

from katas.kyu_6.balance_the_arrays import balance


class BalanceTheArraysTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(balance(['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b'],
                                ['c', 'c', 'c', 'c', 'c', 'd', 'd', 'd']))

    def test_true_2(self):
        self.assertTrue(balance(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g'],
                                ['h', 'h', 'i', 'j', 'k', 'l', 'm', 'n']))

    def test_true_3(self):
        self.assertTrue(balance(['a'], ['c']))

    def test_false_1(self):
        self.assertFalse(balance(['a', 'a'], ['c']))

    def test_false_2(self):
        self.assertFalse(balance(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g'],
                                 ['h', 'h', 'i', 'j', 'k', 'l', 'm', 'm']))
