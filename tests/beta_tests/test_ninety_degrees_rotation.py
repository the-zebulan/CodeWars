import unittest

from katas.beta.ninety_degrees_rotation import rotate


class RotateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(rotate([[1, 2], [3, 4]]), [[3, 1], [4, 2]])

    def test_equals_2(self):
        self.assertEqual(rotate([[3, 1], [4, 2]]), [[4, 3], [2, 1]])
