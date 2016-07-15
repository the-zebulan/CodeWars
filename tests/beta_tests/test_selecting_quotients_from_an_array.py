import unittest

from katas.beta.selecting_quotients_from_an_array import sel_quot


class SelectingQuotientsTestCase(unittest.TestCase):
    def setUp(self):
        self.lst = [2, 4, 27, 16, 9, 15, 25, 6, 12,
                    83, 24, 49, 7, 5, 94, 12, 6]

    def test_equals(self):
        self.assertEqual(sel_quot(self.lst, 6, 'Odd'),
                         [(7, (49, 7)), (47, (94, 2))])

    def test_equals_2(self):
        self.assertEqual(sel_quot(self.lst, 6, 'even'), [
            (6, (12, 2)), (6, (24, 4)), (8, (16, 2)), (12, (24, 2))
        ])

    def test_equals_3(self):
        self.assertEqual(sel_quot(self.lst, 6), [
            (6, (12, 2)), (6, (24, 4)), (7, (49, 7)),
            (8, (16, 2)), (12, (24, 2)), (47, (94, 2))
        ])
