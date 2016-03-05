import unittest

from Kyu_6.prize_draw import rank


class PrizeDrawTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(rank('Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden',
                              [1, 3, 5, 5, 3, 6], 2), 'Matthew')

    def test_equals_2(self):
        self.assertEqual(rank('COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH',
                              [1, 4, 4, 5, 2, 1], 4), 'PauL')

    def test_equals_3(self):
        self.assertEqual(rank(
            'Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin',
            [4, 2, 1, 4, 3, 1, 2], 4), 'Benjamin')

    def test_equals_4(self):
        self.assertEqual(rank('Lagon,Lily', [1, 5], 2), 'Lagon')

    def test_equals_5(self):
        self.assertEqual(rank(
            'Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin',
            [4, 2, 1, 4, 3, 1, 2], 8), 'Not enough participants')

    def test_equals_6(self):
        self.assertEqual(rank('', [4, 2, 1, 4, 3, 1, 2], 6), 'No participants')


if __name__ == '__main__':
    unittest.main()
