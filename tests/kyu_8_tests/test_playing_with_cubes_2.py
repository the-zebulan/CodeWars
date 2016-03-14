import unittest

from kyu_8.playing_with_cubes_2 import Cube


class CubeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Cube(10).get_side(), 10)

    def test_equals_2(self):
        self.assertEqual(Cube().get_side(), 0)


if __name__ == '__main__':
    unittest.main()
