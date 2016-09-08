import unittest

from katas.kyu_7.shortest_word import find_short


class ShortestWordTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(find_short(
            'turns out random test cases are easier than writing out basic '
            'ones'
        ), 3)

    def test_equal_2(self):
        self.assertEqual(find_short(
            'turns out random test cases are easier than writing out basic '
            'ones'
        ), 3)

    def test_equal_3(self):
        self.assertEqual(
            find_short('lets talk about javascript the best language'), 3
        )

    def test_equal_4(self):
        self.assertEqual(
            find_short('i want to travel the world writing code one day'), 1
        )

    def test_equal_5(self):
        self.assertEqual(
            find_short('Lets all go on holiday somewhere very cold'), 2
        )
