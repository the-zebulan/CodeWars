import unittest

from kyu_8.grasshopper_messi_goals import (
    champions_league_goals, copa_del_rey_goals, la_liga_goals, total_goals
)


class MessiTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(champions_league_goals, 10)

    def test_equals_2(self):
        self.assertEqual(copa_del_rey_goals, 5)

    def test_equals_3(self):
        self.assertEqual(la_liga_goals, 43)

    def test_equals_4(self):
        self.assertEqual(total_goals, 58)


if __name__ == '__main__':
    unittest.main()
