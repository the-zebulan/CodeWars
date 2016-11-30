import unittest

from katas.kyu_7.identical_elements import duplicate_elements


class DuplicateElementsTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]))

    def test_true_2(self):
        self.assertTrue(duplicate_elements([9, 8, 7], [8, 1, 3]))

    def test_true_3(self):
        self.assertTrue(duplicate_elements(
            [2398632, 9172846, 4728162], [2398632, 9235623, 8235492]))

    def test_true_4(self):
        self.assertTrue(duplicate_elements(
            [-2, -4, -6, -8], [-2, -3, -5, -7]))

    def test_true_5(self):
        self.assertTrue(duplicate_elements([-9, -8, -7], [-8, -1, -3]))

    def test_true_6(self):
        self.assertTrue(duplicate_elements(
            [-2398632, -9172846, -4728162], [-2398632, -9235623, -8235492]))

    def test_false_1(self):
        self.assertFalse(duplicate_elements([1, 3, 5, 7, 9], [2, 4, 6, 8]))

    def test_false_2(self):
        self.assertFalse(duplicate_elements([9, 8, 7], [6, 5, 4]))

    def test_false_3(self):
        self.assertFalse(duplicate_elements([], [9, 8, 7, 6, 5]))

    def test_false_4(self):
        self.assertFalse(duplicate_elements([9, 8, 7, 6, 5], []))

    def test_false_5(self):
        self.assertFalse(duplicate_elements([], []))
