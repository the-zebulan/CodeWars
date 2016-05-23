import unittest

from katas.kyu_7.competitive_eating_scoreboard import scoreboard


class ScoreboardTestCase(unittest.TestCase):
    def test_equals_1(self):
        self.assertEqual(scoreboard([
            {'name': 'Billy The Beast', 'chickenwings': 17,
             'hamburgers': 7, 'hotdogs': 8},
            {'name': 'Habanero Hillary', 'chickenwings': 5,
             'hamburgers': 17, 'hotdogs': 11},
            {'name': 'Joey Jaws', 'chickenwings': 8, 'hamburgers': 8,
             'hotdogs': 15},
            {'name': 'Big Bob', 'chickenwings': 20, 'hamburgers': 4,
             'hotdogs': 11}]),
            [{'name': 'Big Bob', 'score': 134},
             {'name': 'Billy The Beast', 'score': 122},
             {'name': 'Habanero Hillary', 'score': 98},
             {'name': 'Joey Jaws', 'score': 94}]
        )

    def test_equals_2(self):
        self.assertEqual(scoreboard([
            {'name': 'Big Bob', 'chickenwings': 20, 'hamburgers': 4,
             'hotdogs': 11}]),
            [{'name': 'Big Bob', 'score': 134}]
        )

    def test_equals_3(self):
        self.assertEqual(scoreboard([
            {'name': 'Joey Jaws', 'chickenwings': 8, 'hamburgers': 8,
             'hotdogs': 15},
            {'name': 'Big Bob', 'chickenwings': 20, 'hamburgers': 4,
             'hotdogs': 11}]),
            [{'name': 'Big Bob', 'score': 134},
             {'name': 'Joey Jaws', 'score': 94}]
        )

    def test_equals_4(self):
        self.assertEqual(scoreboard([
            {'name': 'Joey Jaws', 'chickenwings': 0, 'hamburgers': 1,
             'hotdogs': 1},
            {'name': 'Big Bob', 'chickenwings': 1, 'hambrgers': 0,
             'hotdogs': 0}]),
            [{'name': 'Big Bob', 'score': 5},
             {'name': 'Joey Jaws', 'score': 5}]
        )

    def test_equals_5(self):
        self.assertEqual(scoreboard([]), [])


if __name__ == '__main__':
    unittest.main()
