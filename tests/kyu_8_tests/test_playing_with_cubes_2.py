import unittest

from katas.kyu_8.playing_with_cubes_2 import Cube


class CubeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(Cube(10).get_side(), 10)

    def test_equal_2(self):
        self.assertEqual(Cube().get_side(), 0)

    def test_equal_3(self):
        c = Cube(2)
        c.set_side(3)
        self.assertEqual(c.get_side(), 3)
