import unittest

from katas.kyu_7.is_this_a_triangle import is_triangle


class IsTriangleTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(is_triangle(1, 2, 2))

    def test_true_2(self):
        self.assertTrue(is_triangle(4, 2, 3))

    def test_true_3(self):
        self.assertTrue(is_triangle(5, 1, 5))

    def test_true_4(self):
        self.assertTrue(is_triangle(2, 2, 2))

    def test_false_1(self):
        self.assertFalse(is_triangle(7, 2, 2))

    def test_false_2(self):
        self.assertFalse(is_triangle(1, 2, 3))

    def test_false_3(self):
        self.assertFalse(is_triangle(1, 3, 2))

    def test_false_4(self):
        self.assertFalse(is_triangle(3, 1, 2))

    def test_false_5(self):
        self.assertFalse(is_triangle(5, 1, 2))

    def test_false_6(self):
        self.assertFalse(is_triangle(1, 2, 5))

    def test_false_7(self):
        self.assertFalse(is_triangle(2, 5, 1))

    def test_false_8(self):
        self.assertFalse(is_triangle(-1, 2, 3))

    def test_false_9(self):
        self.assertFalse(is_triangle(1, -2, 3))

    def test_false_10(self):
        self.assertFalse(is_triangle(1, 2, -3))

    def test_false_11(self):
        self.assertFalse(is_triangle(0, 2, 3))
