import unittest

from beta.credit_card_validifier import credit


class CreditTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(credit(6011364837263748), 'Discover')

    def test_equals_2(self):
        self.assertEqual(credit(5318273647283745), 'Master')

    def test_equals_3(self):
        self.assertEqual(credit(12345678910), 'Invalid')

    def test_equals_4(self):
        self.assertEqual(credit(371236473823676), 'AMEX')

    def test_equals_5(self):
        self.assertEqual(credit(4128374839283), 'VISA')


if __name__ == '__main__':
    unittest.main()
