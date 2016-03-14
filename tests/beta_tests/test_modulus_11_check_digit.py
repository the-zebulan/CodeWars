import unittest

from beta.modulus_11_check_digit import add_check_digit


class AddCheckDigitTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(add_check_digit('111111111'), '1111111118')

    def test_equals_2(self):
        self.assertEqual(add_check_digit('12388878'), '123888782')

    def test_equals_3(self):
        self.assertEqual(add_check_digit('036532'), '0365327')

    def test_equals_4(self):
        self.assertEqual(add_check_digit('9735597355'), '97355973550')


if __name__ == '__main__':
    unittest.main()
