import unittest

from katas.kyu_6.simple_card_game import winner


class WinnerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(winner(list('A78'), list('K59')), 'Steve wins 2 to 1')

    def test_equals_2(self):
        self.assertEqual(winner(list('K245432KAT'), list('Q346435A87')),
                         'Josh wins 4 to 3')

    def test_equals_3(self):
        self.assertEqual(winner(
            list('9QQAT7693Q43744Q6568Q8484AJA8JK36T4557K9'),
            list('TQK284TA753A9KJ75337JQK9Q3696K7AQ2752AJ4')),
            'Steve wins 20 to 18')


if __name__ == '__main__':
    unittest.main()
