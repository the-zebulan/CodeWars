import unittest

from kyu_7.regex_validate_pin_code import validate_pin


class ValidatePinTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate_pin('1111'))

    def test_true_2(self):
        self.assertTrue(validate_pin('123456'))

    def test_false(self):
        self.assertFalse(validate_pin(''))

    def test_false_2(self):
        self.assertFalse(validate_pin('1'))

    def test_false_3(self):
        self.assertFalse(validate_pin('1234567'))

    def test_false_4(self):
        self.assertFalse(validate_pin('-1234'))


if __name__ == '__main__':
    unittest.main()
