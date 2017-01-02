import unittest
from random import random

from katas.beta.sortable_shapes import (
    Circle, CustomShape, Rectangle, Square, Triangle)


class SortableShapesTestCase(unittest.TestCase):
    def test_equal_1(self):
        expected = [
            CustomShape(1.1234),
            Square(1.1234),
            Circle(1.1234),
            Triangle(5, 2),
            Triangle(3, 4),
            Rectangle(4, 2),
            CustomShape(16.1)
        ]
        self.assertEqual(
            sorted(sorted(expected, key=lambda _: random())), expected)
