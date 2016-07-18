import unittest

from katas.beta.builtin_product_function import product


class ProductTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(product((2, 3)), 6)

    def test_equal_2(self):
        self.assertEqual(product((4, 5)), 20)

    def test_equal_3(self):
        self.assertEqual(product((3, 4, 5, 6)), 360)
