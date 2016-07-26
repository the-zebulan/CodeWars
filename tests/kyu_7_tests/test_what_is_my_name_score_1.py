import unittest

from katas.kyu_7.what_is_my_name_score_1 import name_score


class NameScoreTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(name_score('Mary Jane'), {'Mary Jane': 20})

    def test_equal_2(self):
        self.assertEqual(name_score('Luke Skywalker'),
                         {'Luke Skywalker': 41})

    def test_equal_3(self):
        self.assertEqual(name_score('Zoe Andrews'), {'Zoe Andrews': 23})

    def test_equal_4(self):
        self.assertEqual(name_score('Double  Space'), {'Double  Space': 25})

    def test_equal_5(self):
        self.assertEqual(name_score('Greg Z MacDonald'),
                         {'Greg Z MacDonald': 26})
