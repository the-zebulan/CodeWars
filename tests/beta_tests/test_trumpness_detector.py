import unittest

from katas.beta.trumpness_detector import trump_detector


class TrumpDetectorTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(trump_detector('I will build a huge wall'), 0)

    def test_equal_2(self):
        self.assertEqual(trump_detector('HUUUUUGEEEE WAAAAAALL'), 4)

    def test_equal_3(self):
        self.assertEqual(trump_detector(
            'MEXICAAAAAAAANS GOOOO HOOOMEEEE'
        ), 2.5)

    def test_equal_4(self):
        self.assertEqual(trump_detector(
            'America NUUUUUKEEEE Oooobaaaamaaaaa'
        ), 1.89)

    def test_equal_5(self):
        self.assertEqual(trump_detector(
            'listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT'
        ), 1.56)
