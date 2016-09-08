import unittest

from katas.kyu_7.to_leet_speak import to_leet_speak


class LeetSpeakTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(to_leet_speak('LEET'), '1337')

    def test_equal_2(self):
        self.assertEqual(to_leet_speak('CODEWARS'), '(0D3W@R$')

    def test_equal_3(self):
        self.assertEqual(to_leet_speak('HELLO WORLD'), '#3110 W0R1D')

    def test_equal_4(self):
        self.assertEqual(to_leet_speak('LOREM IPSUM DOLOR SIT AMET'),
                         '10R3M !P$UM D010R $!7 @M37')

    def test_equal_5(self):
        self.assertEqual(
            to_leet_speak('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'),
            '7#3 QU!(K 8R0WN F0X JUMP$ 0V3R 7#3 1@2Y D06'
        )
