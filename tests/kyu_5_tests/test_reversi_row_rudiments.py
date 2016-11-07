import unittest

from katas.kyu_5.reversi_row_rudiments import reversi_row


class ReversiRowTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(reversi_row([]), '........')

    def test_equal_2(self):
        self.assertEqual(reversi_row([0]), '*.......')

    def test_equal_3(self):
        self.assertEqual(reversi_row([0, 1]), '*O......')

    def test_equal_4(self):
        self.assertEqual(reversi_row([0, 7, 4]), '*...*..O')

    def test_equal_5(self):
        self.assertEqual(reversi_row([3]), '...*....')

    def test_equal_6(self):
        self.assertEqual(reversi_row([3, 4]), '...*O...')

    def test_equal_7(self):
        self.assertEqual(reversi_row([3, 4, 5]), '...***..')

    def test_equal_8(self):
        self.assertEqual(reversi_row([2, 1, 0]), '***.....')

    def test_equal_9(self):
        self.assertEqual(reversi_row([0, 1, 4, 3, 2]), '*****...')

    def test_equal_10(self):
        self.assertEqual(reversi_row([0, 1, 7, 2, 3]), '****...*')

    def test_equal_11(self):
        self.assertEqual(reversi_row([3, 2, 7, 1, 0]), '****...*')

    def test_equal_12(self):
        self.assertEqual(reversi_row([3, 4, 5, 6, 0, 2]), '*.OOOOO.')

    def test_equal_13(self):
        self.assertEqual(reversi_row([0, 1, 2, 3, 4, 5, 6, 7]), '*******O')

    def test_equal_14(self):
        self.assertEqual(reversi_row([7, 0, 1]), 'O*.....*')

    def test_equal_15(self):
        self.assertEqual(reversi_row([0, 7, 6]), '*.....*O')

    def test_equal_16(self):
        self.assertEqual(reversi_row([1, 0, 2, 3, 4, 5, 6, 7]), 'OOOOOOOO')

    def test_equal_17(self):
        self.assertEqual(reversi_row([5, 1, 3, 4, 6]), '.O.*O**.')

    def test_equal_18(self):
        self.assertEqual(reversi_row([1, 7, 0, 5, 6, 4]), '**..OO*O')
