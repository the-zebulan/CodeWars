import unittest

from katas.kyu_5.tic_tac_toe_checker import isSolved


class TicTacToeTestCase(unittest.TestCase):
    """ if the board is not solved: return -1
        if it's a draw: return 0
        if X (1) won: return 1
        if O (2) won: return 2
    """

    def test_equal_1(self):
        """ board is not solved yet """
        self.assertEqual(isSolved([
            [0, 0, 1],
            [0, 1, 2],
            [2, 1, 0]
        ]), -1)

    def test_equal_2(self):
        """ cat's game (draw) """
        self.assertEqual(isSolved([
            [1, 2, 1],
            [1, 1, 2],
            [2, 1, 2]]
        ), 0)

    def test_equal_3(self):
        """ horizontal row win for O (2) """
        self.assertEqual(isSolved([
            [2, 2, 2],
            [1, 2, 1],
            [1, 1, 2]
        ]), 2)

    def test_equal_4(self):
        """ vertical row win for O (2) """
        self.assertEqual(isSolved([
            [2, 1, 2],
            [1, 1, 2],
            [1, 2, 2]
        ]), 2)

    def test_equal_5(self):
        """ diagonal row win for O (2) """
        self.assertEqual(isSolved([
            [2, 1, 2],
            [1, 2, 1],
            [1, 1, 2]
        ]), 2)

    def test_equal_6(self):
        """ horizontal row win for X (1) """
        self.assertEqual(isSolved([
            [1, 1, 1],
            [1, 2, 1],
            [2, 1, 2]
        ]), 1)

    def test_equal_7(self):
        """ vertical row win for X (1) """
        self.assertEqual(isSolved([
            [2, 1, 1],
            [1, 2, 1],
            [1, 2, 1]
        ]), 1)

    def test_equal_8(self):
        """ diagonal row win for X (1) """
        self.assertEqual(isSolved([
            [2, 1, 1],
            [1, 1, 1],
            [1, 2, 2]
        ]), 1)
