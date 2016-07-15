import unittest

from katas.kyu_7.ean_validation import validate_ean


class ValidateEANTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate_ean('4003301018398'))

    def test_true_2(self):
        self.assertTrue(validate_ean("9783815820865"))

    def test_true_3(self):
        self.assertTrue(validate_ean("9783827317100"))

    def test_false(self):
        self.assertFalse(validate_ean("0000000000010"))

    def test_false_2(self):
        self.assertFalse(validate_ean('4003301018392'))

    def test_false_3(self):
        self.assertFalse(validate_ean("9783815820864"))
