import unittest

from katas.kyu_7.bug_fixing_reducing_problems import calculate_total


class CalculateTotalTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(calculate_total([1, 2, 2], [1, 0, 0]))

    def test_true_2(self):
        self.assertTrue(calculate_total([57, 2, 1], []))

    def test_false(self):
        self.assertFalse(calculate_total([6, 45, 1], [1, 55, 0]))

    def test_false_2(self):
        self.assertFalse(calculate_total([], [3, 4, 3]))

    def test_false_3(self):
        self.assertFalse(calculate_total([], []))


if __name__ == '__main__':
    unittest.main()
