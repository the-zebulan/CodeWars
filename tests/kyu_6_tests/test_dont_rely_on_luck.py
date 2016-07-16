import unittest
from random import randint

from katas.kyu_6.dont_rely_on_luck import guess


class DontRelyOnLuckTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(guess, randint(1, 100))

    def test_not_equal_1(self):
        self.assertNotEqual(guess, randint(1, 100))
