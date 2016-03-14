import unittest

from kyu_8.validate_code_with_simple_regex import validate_code


class ValidateCodeTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate_code(123))

    def test_true_2(self):
        self.assertTrue(validate_code(248))

    def test_true_3(self):
        self.assertTrue(validate_code(321))

    def test_false(self):
        self.assertFalse(validate_code(8))

    def test_false_2(self):
        self.assertFalse(validate_code(9453))


if __name__ == '__main__':
    unittest.main()
