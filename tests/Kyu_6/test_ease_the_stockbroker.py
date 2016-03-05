import unittest

from Kyu_6.ease_the_stockbroker import balance_statement


class BalanceStatementTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(balance_statement(
            'ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG '
            '20 580.1 B'), 'Buy: 29499 Sell: 0')

    def test_equals_2(self):
        self.assertEqual(balance_statement(''), 'Buy: 0 Sell: 0')

    def test_equals_3(self):
        self.assertEqual(balance_statement(
            'GOOG 300 542.0 B, AAPL 50 145.0 B, CSCO 250.0 29 B, '
            'GOOG 200 580.0 S'),
            'Buy: 169850 Sell: 116000; Badly formed 1: CSCO 250.0 29 B ;')

    def test_equals_4(self):
        self.assertEqual(balance_statement(
            'CAP 1300 .2 B, CLH16.NYM 50 56 S, OWW 1000 11 S, OGG 20 580.1 S'),
            'Buy: 260 Sell: 11602; Badly formed 2: CLH16.NYM 50 56 S ;OWW 10'
            '00 11 S ;')


if __name__ == '__main__':
    unittest.main()
