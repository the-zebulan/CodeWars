import unittest

from katas.kyu_7.volume_of_a_cup import cup_volume


class CupVolumeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(cup_volume(1, 1, 1), 0.79)

    def test_equal_2(self):
        self.assertEqual(cup_volume(10, 8, 10), 638.79)

    def test_equal_3(self):
        self.assertEqual(cup_volume(1000, 1000, 1000), 785398163.4)

    def test_equal_4(self):
        self.assertEqual(cup_volume(13.123, 123.12, 1), 4436.57)

    def test_equal_5(self):
        self.assertEqual(cup_volume(5, 12, 31), 1858.51)
