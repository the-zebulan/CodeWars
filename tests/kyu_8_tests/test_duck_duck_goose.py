import unittest

from katas.kyu_8.duck_duck_goose import duck_duck_goose


class Player(object):
    """ This class is needed for testing this kata """
    def __init__(self, name):
        self.name = name


class DuckDuckGooseTestCase(unittest.TestCase):
    def setUp(self):
        self.players = [Player(a) for a in 'abcdcefghz']

    def test_equal_1(self):
        self.assertEqual(duck_duck_goose(self.players, 1),  'a')

    def test_equal_2(self):
        self.assertEqual(duck_duck_goose(self.players, 3),  'c')

    def test_equal_3(self):
        self.assertEqual(duck_duck_goose(self.players, 10), 'z')

    def test_equal_4(self):
        self.assertEqual(duck_duck_goose(self.players, 20), 'z')

    def test_equal_5(self):
        self.assertEqual(duck_duck_goose(self.players, 30), 'z')

    def test_equal_6(self):
        self.assertEqual(duck_duck_goose(self.players, 18), 'g')

    def test_equal_7(self):
        self.assertEqual(duck_duck_goose(self.players, 28), 'g')

    def test_equal_8(self):
        self.assertEqual(duck_duck_goose(self.players, 12), 'b')

    def test_equal_9(self):
        self.assertEqual(duck_duck_goose(self.players, 2),  'b')

    def test_equal_10(self):
        self.assertEqual(duck_duck_goose(self.players, 7),  'f')
