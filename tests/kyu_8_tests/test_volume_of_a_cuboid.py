import unittest

from katas.kyu_8.volume_of_a_cuboid import get_volume_of_cuboid


class GetVolumeOfCuboidTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_volume_of_cuboid(1, 2, 2), 4)

    def test_equal_2(self):
        self.assertEqual(get_volume_of_cuboid(6.3, 2, 5), 63)
