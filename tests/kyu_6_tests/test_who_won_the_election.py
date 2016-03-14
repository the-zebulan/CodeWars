import unittest

from Kyu_6.who_won_the_election import getWinner


class GetWinnerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(getWinner('A'), 'A')

    def test_equals_2(self):
        self.assertEqual(getWinner(('A', 'A', 'A', 'B', 'B', 'B', 'A')), 'A')

    def test_none(self):
        self.assertIsNone(getWinner(('A', 'A', 'A', 'B', 'B', 'B')))

    def test_none_2(self):
        self.assertIsNone(getWinner(('A', 'A', 'A', 'B', 'C', 'B')))

    def test_none_3(self):
        self.assertIsNone(getWinner(('A', 'A', 'B', 'B', 'C')))


if __name__ == '__main__':
    unittest.main()
