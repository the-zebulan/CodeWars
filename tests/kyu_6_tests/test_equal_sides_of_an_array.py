import unittest

from katas.kyu_6.equal_sides_of_an_array import find_even_index


class FindEvenIndexTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)

    def test_equals_2(self):
        self.assertEqual(find_even_index([1, 100, 50, -51, 1, 1]), 1)

    def test_equals_3(self):
        self.assertEqual(find_even_index([1, 2, 3, 4, 5, 6]), -1)

    def test_equals_4(self):
        self.assertEqual(find_even_index([20, 10, 30, 10, 10, 15, 35]), 3)

    def test_equals_5(self):
        self.assertEqual(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)

    def test_equals_6(self):
        self.assertEqual(find_even_index([10, -80, 10, 10, 15, 35, 20]), 6)

    def test_equals_7(self):
        self.assertEqual(find_even_index(range(1, 100)), -1)

    def test_equals_8(self):
        self.assertEqual(find_even_index([0, 0, 0, 0, 0]), 0)

    def test_equals_9(self):
        self.assertEqual(find_even_index([-1, -2, -3, -4, -3, -2, -1]), 3)

    def test_equals_10(self):
        self.assertEqual(find_even_index(range(-100, -1)), -1)
