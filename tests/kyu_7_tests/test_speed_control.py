import unittest

from katas.kyu_7.speed_control import gps


class GPSTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(gps(
            15, [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]), 74)

    def test_equals_2(self):
        self.assertEqual(gps(
            15, [0.0, 0.15, 0.42, 0.67, 1.0, 1.15, 1.5, 1.65, 1.8, 2]), 84)

    def test_equals_3(self):
        self.assertEqual(gps(
            20, [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]), 41)

    def test_equals_4(self):
        self.assertEqual(gps(12, [
            0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1,
            2.31, 2.52, 3.25
        ]), 219)

    def test_equals_5(self):
        self.assertEqual(gps(20, [
            0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4,
            2.64, 2.88, 3.12, 3.36, 3.6, 3.84
        ]), 81)

    def test_equals_6(self):
        self.assertEqual(gps(10, []), 0)
