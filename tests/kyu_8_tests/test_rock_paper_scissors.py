import unittest

from katas.kyu_8.rock_paper_scissors import rps


class RockPaperScissorsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(rps('rock', 'scissors'), 'Player 1 won!')

    def test_equals_2(self):
        self.assertEqual(rps('scissors', 'paper'), 'Player 1 won!')

    def test_equals_3(self):
        self.assertEqual(rps('paper', 'rock'), 'Player 1 won!')

    def test_equals_4(self):
        self.assertEqual(rps('scissors', 'rock'), 'Player 2 won!')

    def test_equals_5(self):
        self.assertEqual(rps('paper', 'scissors'), 'Player 2 won!')

    def test_equals_6(self):
        self.assertEqual(rps('rock', 'paper'), 'Player 2 won!')

    def test_equals_7(self):
        self.assertEqual(rps('rock', 'rock'), 'Draw!')

    def test_equals_8(self):
        self.assertEqual(rps('scissors', 'scissors'), 'Draw!')

    def test_equals_9(self):
        self.assertEqual(rps('paper', 'paper'), 'Draw!')


if __name__ == '__main__':
    unittest.main()
