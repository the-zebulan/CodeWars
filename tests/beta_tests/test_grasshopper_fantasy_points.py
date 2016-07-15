import unittest

import katas.beta.grasshopper_fantasy_points as g


class GrasshopperTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(g.assists, 3)

    def test_equal_2(self):
        self.assertEqual(g.crosses, 3)

    def test_equal_3(self):
        self.assertEqual(g.chancesCreated, 4)

    def test_equal_4(self):
        self.assertEqual(g.goals, 4)

    def test_equal_5(self):
        self.assertEqual(g.shotsOnTarget, 5)

    def test_equal_6(self):
        self.assertEqual(g.successfulDribbles, 10)

    def test_equal_7(self):
        self.assertEqual(g.points, 89)
