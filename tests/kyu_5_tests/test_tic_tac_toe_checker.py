import unittest

from Kyu_5.tic_tac_toe_checker import isSolved


class TicTacToeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(isSolved([[0, 0, 1], [0, 1, 2], [2, 1, 0]]), -1)

    def test_equals_2(self):
        self.assertEqual(isSolved([[1, 2, 1], [1, 1, 2], [2, 1, 2]]), 0)


if __name__ == '__main__':
    unittest.main()
