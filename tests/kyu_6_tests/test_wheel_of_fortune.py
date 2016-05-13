import unittest

from katas.kyu_6.wheel_of_fortune import winner


class WinnerTestCase(unittest.TestCase):
    def setUp(self):
        self.c1 = {'name': "Bob", 'scores': [10, 65]}
        self.c2 = {'name': "Bill", 'scores': [90, 5]}
        self.c3 = {'name': "Jennifer", 'scores': [55]}
        self.c4 = {'name': "John", 'scores': [5, 15]}
        self.c5 = {'name': "Brad", 'scores': [3, 15]}
        self.c6 = {'name': "Laurel", 'scores': [5, 12]}
        self.c7 = {'name': "Charlie", 'scores': [5, 105]}
        self.c8 = {'name': "Paul", 'scores': [80, 25]}
        self.c9 = {'name': "Marc", 'scores': [80, 25]}
        self.c10 = {'name': "Oliver", 'scores': [80, 25]}
        self.c11 = {'name': "Bruce", 'scores': []}
        self.c12 = {'name': "Alfred", 'scores': [10, 15, 20]}
        self.c13 = {'scores': [10, 20]}
        self.c14 = {'name': "Cheater"}
        self.c15 = {'name': "Robert", 'scores': [45]}
        self.c16 = {'name': "Rob", 'scores': [40, 45]}
        self.c17 = {'name': "Ned", 'scores': [10]}
        self.c18 = {'name': "Gandalf", 'scores': [85]}

    def test_equal_1(self):
        self.assertEqual(winner([self.c1, self.c2, self.c3]), "Bill")

    def test_equal_2(self):
        self.assertEqual(winner([self.c15, self.c16, self.c17]), "Rob")

    def test_equal_3(self):
        self.assertEqual(winner([self.c15, self.c17, self.c18]), "Gandalf")

    def test_equal_4(self):
        self.assertEqual(winner([self.c16, self.c17, self.c18]), "Rob")

    def test_equal_5(self):
        self.assertEqual(winner([self.c18, self.c17, self.c16]), "Gandalf")

    def test_equal_6(self):
        self.assertEqual(winner([
            {'name': 'Grawl', 'scores': [80, 95]},
            {'name': 'Death Gaia', 'scores': [60, 15]},
            {'name': 'Helmat', 'scores': [60]}
        ]), 'Death Gaia')

    def test_false_1(self):
        self.assertFalse(winner([]))

    def test_false_2(self):
        self.assertFalse(winner([self.c1]))

    def test_false_3(self):
        self.assertFalse(winner([self.c1, self.c2]))

    def test_false_4(self):
        self.assertFalse(winner([self.c1, self.c2, self.c3, self.c4]))

    def test_false_5(self):
        self.assertFalse(winner([self.c1, self.c11, self.c3]))

    def test_false_6(self):
        self.assertFalse(winner([self.c1, self.c3, self.c12]))

    def test_false_7(self):
        self.assertFalse(winner([self.c1, self.c2, self.c6]))

    def test_false_8(self):
        self.assertFalse(winner([self.c1, self.c7, self.c2]))

    def test_false_9(self):
        self.assertFalse(winner([self.c8, self.c9, self.c10]))

    def test_false_10(self):
        self.assertFalse(winner([self.c1, self.c2, self.c13]))

    def test_false_11(self):
        self.assertFalse(winner([self.c1, self.c14, self.c2]))

    def test_false_12(self):
        self.assertFalse(winner([
            {'name': 'Gildorome', 'scores': [10, 90]},
            {'name': 'Bostori', 'scores': [50, 56]},
            {'name': 'Grawl', 'scores': [85]}])
        )


if __name__ == '__main__':
    unittest.main()
