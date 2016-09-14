import unittest

from katas.kyu_7.simple_sequence_validator import validate_sequence


class ValidateSequenceTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(validate_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_true_2(self):
        self.assertTrue(validate_sequence([2, 4, 6, 8, 10]))

    def test_true_3(self):
        self.assertTrue(validate_sequence([0, 2, 4, 6, 8]))

    def test_true_4(self):
        self.assertTrue(validate_sequence([1, 3, 5, 7, 9]))

    def test_false_1(self):
        self.assertFalse(validate_sequence([1, 2, 3, 4, 5, 8, 7, 8, 9]))

    def test_false_2(self):
        self.assertFalse(validate_sequence([1, 2, 4, 8, 16, 32, 64]))

    def test_false_3(self):
        self.assertFalse(validate_sequence([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))
