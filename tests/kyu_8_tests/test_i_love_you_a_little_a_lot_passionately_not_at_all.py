import unittest

from katas.kyu_8.i_love_you_a_little_a_lot_passionately_not_at_all import \
    how_much_i_love_you


class HowMuchILoveYou(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(how_much_i_love_you(1), 'I love you')

    def test_equal_2(self):
        self.assertEqual(how_much_i_love_you(2), 'a little')

    def test_equal_3(self):
        self.assertEqual(how_much_i_love_you(3), 'a lot')

    def test_equal_4(self):
        self.assertEqual(how_much_i_love_you(4), 'passionately')

    def test_equal_5(self):
        self.assertEqual(how_much_i_love_you(5), 'madly')

    def test_equal_6(self):
        self.assertEqual(how_much_i_love_you(6), 'not at all')

    def test_equal_7(self):
        self.assertEqual(how_much_i_love_you(7), 'I love you')

    def test_equal_8(self):
        self.assertEqual(how_much_i_love_you(8), 'a little')

    def test_equal_9(self):
        self.assertEqual(how_much_i_love_you(9), 'a lot')

    def test_equal_10(self):
        self.assertEqual(how_much_i_love_you(10), 'passionately')

    def test_equal_11(self):
        self.assertEqual(how_much_i_love_you(11), 'madly')

    def test_equal_12(self):
        self.assertEqual(how_much_i_love_you(12), 'not at all')
