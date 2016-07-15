import unittest

from katas.kyu_8.grasshopper_shopping_list import (
    frenchFries, salads, sandwiches, wraps, totalPrice
)


class ShoppingListTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(frenchFries, 10)

    def test_equals_2(self):
        self.assertEqual(salads, 6)

    def test_equals_3(self):
        self.assertEqual(sandwiches, 4)

    def test_equals_4(self):
        self.assertEqual(wraps, 5)

    def test_equals_5(self):
        self.assertEqual(totalPrice, 118.5)
