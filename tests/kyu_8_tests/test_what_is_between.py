import unittest

from katas.kyu_8.what_is_between import between


class WhatIsBetweenTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(between(1, 4), range(1, 4 + 1))

    def test_equal_2(self):
        self.assertEqual(between(5, 500), range(5, 500 + 1))

    def test_equal_3(self):
        self.assertEqual(between(-10, 10), range(-10, 10 + 1))

    def test_equal_4(self):
        self.assertEqual(between(-2, 2), range(-2, 2 + 1))

    def test_equal_5(self):
        self.assertEqual(between(49, 67), range(49, 67 + 1))

    def test_equal_6(self):
        self.assertEqual(between(789, 1102), range(789, 1102 + 1))

    def test_equal_7(self):
        self.assertEqual(between(32, 99), range(32, 99 + 1))

    def test_equal_8(self):
        self.assertEqual(between(0, 0), range(0, 0 + 1))
