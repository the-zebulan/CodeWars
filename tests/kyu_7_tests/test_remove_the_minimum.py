import unittest

from katas.kyu_7.remove_the_minimum import remove_smallest


class RemoveSmallestTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])

    def test_equals_2(self):
        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])

    def test_equals_3(self):
        self.assertEqual(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1])

    def test_equals_4(self):
        self.assertEqual(remove_smallest([]), [])
