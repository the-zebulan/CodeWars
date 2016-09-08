import unittest

from katas.kyu_7.find_the_volume_of_a_cone import volume


class ConeVolumeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(volume(7, 3), 153)

    def test_equal_2(self):
        self.assertEqual(volume(56, 30), 98520)

    def test_equal_3(self):
        self.assertEqual(volume(0, 10), 0)

    def test_equal_4(self):
        self.assertEqual(volume(10, 0), 0)

    def test_equal_5(self):
        self.assertEqual(volume(0, 0), 0)
