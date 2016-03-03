import unittest

from Beta.email_validation import validate


class ValidateTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate('abc@example.com'))

    def test_false(self):
        self.assertFalse(validate('_bc@example.com'))

    def test_false_2(self):
        self.assertFalse(validate('sa5 2erd76n@c7ws07u.mobi'))

    def test_false_3(self):
        self.assertFalse(validate('5@a74qljvkfj.it'))


if __name__ == '__main__':
    unittest.main()
