import unittest

from Kyu_6.validate_credit_card_number import validate


class ValidateCreditCardNumberTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate(26))

    def test_true_2(self):
        self.assertTrue(validate(91))

    def test_true_3(self):
        self.assertTrue(validate(1230))

    def test_true_4(self):
        self.assertTrue(validate(2121))

    def test_true_5(self):
        self.assertTrue(validate(912030))

    def test_true_6(self):
        self.assertTrue(validate(2626262626262626))

    def test_true_7(self):
        self.assertTrue(validate(4111111111111111))

    def test_false(self):
        self.assertFalse(validate(1))

    def test_false_2(self):
        self.assertFalse(validate(92))

    def test_false_3(self):
        self.assertFalse(validate(123))

    def test_false_4(self):
        self.assertFalse(validate(1714))

    def test_false_5(self):
        self.assertFalse(validate(922030))

    def test_false_6(self):
        self.assertFalse(validate(8675309))


if __name__ == '__main__':
    unittest.main()
