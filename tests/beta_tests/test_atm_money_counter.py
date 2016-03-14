import unittest

from beta.atm_money_counter import atm


class AtmTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(atm('XSF 1000'), 'Sorry, have no XSF.')

    def test_equals_2(self):
        self.assertEqual(atm('rub 12341'),
                         'Can\'t do 12341 RUB. Value must be divisible by 10!')

    def test_equals_3(self):
        self.assertEqual(atm('10202UAH'),
                         '20 * 500 UAH, 2 * 100 UAH, 1 * 2 UAH')

    def test_equals_4(self):
        self.assertEqual(atm('842 usd'), '8 * 100 USD, 2 * 20 USD, 1 * 2 USD')

    def test_equals_5(self):
        self.assertEqual(atm('euR1000'), '2 * 500 EUR')

    def test_equals_6(self):
        self.assertEqual(atm('sos100'),
                         'Can\'t do 100 SOS. Value must be divisible by 1000!')


if __name__ == '__main__':
    unittest.main()
