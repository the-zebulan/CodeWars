import unittest

from katas.beta.two_fighters_one_winner import declare_winner, Fighter


class DeclareWinnerTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(declare_winner(
            Fighter('Lew', 10, 2), Fighter('Harry', 5, 4), 'Lew'
        ), 'Lew')

    def test_equal_2(self):
        self.assertEqual(declare_winner(
            Fighter('Lew', 10, 2), Fighter('Harry', 5, 4), 'Harry'
        ), 'Harry')

    def test_equal_3(self):
        self.assertEqual(declare_winner(
            Fighter('Harald', 20, 5), Fighter('Harry', 5, 4), 'Harry'
        ), 'Harald')

    def test_equal_4(self):
        self.assertEqual(declare_winner(
            Fighter('Harald', 20, 5), Fighter('Harry', 5, 4), 'Harald'
        ), 'Harald')

    def test_equal_5(self):
        self.assertEqual(declare_winner(
            Fighter('Jerry', 30, 3), Fighter('Harald', 20, 5), 'Jerry'
        ), 'Harald')

    def test_equal_6(self):
        self.assertEqual(declare_winner(
            Fighter('Jerry', 30, 3), Fighter('Harald', 20, 5), 'Harald'
        ), 'Harald')
