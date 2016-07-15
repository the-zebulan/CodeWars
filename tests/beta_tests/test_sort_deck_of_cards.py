import unittest

from katas.beta.sort_deck_of_cards import sort_cards


class SortCardsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sort_cards(
            ['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']
        ), ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'])

    def test_equal_2(self):
        self.assertEqual(sort_cards(
            ['Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T']
        ), ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'])

    def test_equal_3(self):
        self.assertEqual(sort_cards(
            ['5', '4', 'T', 'Q', 'K', 'J', '6', '9', '3', '2', '7', 'A', '8']
        ), ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'])
