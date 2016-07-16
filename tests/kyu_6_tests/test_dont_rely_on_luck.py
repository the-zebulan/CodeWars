import unittest
from random import randint, seed

from katas.kyu_6.dont_rely_on_luck import guess


class DontRelyOnLuckTestCase(unittest.TestCase):
    def test_equal_1(self):
        seed(1)
        self.assertEqual(guess, randint(1, 100))

    def test_not_equal_1(self):
        seed(22)
        self.assertNotEqual(guess, randint(1, 100))
