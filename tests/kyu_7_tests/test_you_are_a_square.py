import unittest

from katas.kyu_7.you_are_a_square import is_square


class IsSquareTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_square(4))

    def test_true_2(self):
        self.assertTrue(is_square(25))

    def test_false(self):
        self.assertFalse(is_square(-1))

    def test_false_2(self):
        self.assertFalse(is_square(3))

    def test_false_3(self):
        self.assertFalse(is_square(26))
