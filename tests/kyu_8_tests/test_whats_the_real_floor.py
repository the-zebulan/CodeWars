import unittest

from katas.kyu_8.whats_the_real_floor import get_real_floor


class GetRealFloorTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_real_floor(1), 0)

    def test_equal_2(self):
        self.assertEqual(get_real_floor(0), 0)

    def test_equal_3(self):
        self.assertEqual(get_real_floor(5), 4)

    def test_equal_4(self):
        self.assertEqual(get_real_floor(15), 13)

    def test_equal_5(self):
        self.assertEqual(get_real_floor(-3), -3)
