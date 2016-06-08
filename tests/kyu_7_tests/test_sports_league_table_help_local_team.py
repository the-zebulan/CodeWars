import unittest

from katas.kyu_7.sports_league_table_help_local_team import league_calculate


class LeagueCalculateTestCase(unittest.TestCase):
    def setUp(self):
        self.league_table = [
            ['teamA', 3], ['teamB', 3], ['teamC', 3], ['teamD', 3]
        ]

    def test_equal_1(self):
        self.assertEqual(league_calculate('teamA', 'teamB', 'draw'), [
            ['teamA', 4], ['teamB', 4], ['teamC', 3], ['teamD', 3]
        ])

    def test_equal_2(self):
        self.assertEqual(league_calculate('teamC', 'teamD', 'win'), [
            ['teamC', 6], ['teamA', 4], ['teamB', 4], ['teamD', 3]
        ])

    def test_equal_3(self):
        self.assertEqual(league_calculate('teamA', 'teamC', 'draw'), [
            ['teamC', 7], ['teamA', 5], ['teamB', 4], ['teamD', 3]
        ])

    def test_equal_4(self):
        self.assertEqual(league_calculate('teamB', 'teamD', 'win'), [
            ['teamB', 7], ['teamC', 7], ['teamA', 5], ['teamD', 3]
        ])

    def test_equal_5(self):
        self.assertEqual(league_calculate('teamA', 'teamB', 'win'), [
            ['teamA', 8], ['teamB', 7], ['teamC', 7], ['teamD', 3]
        ])

    def test_equal_6(self):
        self.assertEqual(league_calculate('teamC', 'teamD', 'draw'), [
            ['teamA', 8], ['teamC', 8], ['teamB', 7], ['teamD', 4]
        ])

    def test_equal_7(self):
        self.assertEqual(league_calculate('teamD', 'teamA', 'draw'), [
            ['teamA', 9], ['teamC', 8], ['teamB', 7], ['teamD', 5]
        ])

    def test_equal_8(self):
        self.assertEqual(league_calculate('teamC', 'teamB', 'win'), [
            ['teamC', 11], ['teamA', 9], ['teamB', 7], ['teamD', 5]
        ])

    def test_equal_9(self):
        self.assertEqual(league_calculate('teamB', 'teamD', 'win'), [
            ['teamC', 11], ['teamB', 10], ['teamA', 9], ['teamD', 5]
        ])


if __name__ == '__main__':
    unittest.main()
