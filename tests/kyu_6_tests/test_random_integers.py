import unittest

from katas.kyu_6.random_integers import random_ints


class RandomIntsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sum(random_ints(3, 5)), 5)

    def test_equal_2(self):
        self.assertEqual(sum(random_ints(2, 6)), 6)

    def test_equal_3(self):
        self.assertEqual(len(random_ints(3, 5)), 3)

    def test_equal_4(self):
        self.assertEqual(len(random_ints(2, 6)), 2)
