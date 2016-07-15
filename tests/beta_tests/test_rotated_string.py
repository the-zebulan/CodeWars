import unittest

from katas.beta.rotated_string import is_rotation


class IsRotationTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_rotation('hello', 'ohell'))

    def test_true_2(self):
        self.assertTrue(is_rotation('hello', 'elloh'))

    def test_false(self):
        self.assertFalse(is_rotation('hello', 'lloeh'))

    def test_false_2(self):
        self.assertFalse(is_rotation('hello', 'hellohello'))
