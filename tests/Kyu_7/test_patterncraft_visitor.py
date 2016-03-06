import unittest

from Kyu_7.patterncraft_visitor import Marauder, Marine, TankBullet


class PatterncraftVisitorTestCase(unittest.TestCase):
    def setUp(self):
        self.bullet = TankBullet()
        self.light = Marine()
        self.bullet2 = TankBullet()
        self.armored = Marauder()

    def test_equals(self):
        self.light.accept(self.bullet)
        self.assertEqual(self.light.health, 100 - 21)

    def test_equals_2(self):
        self.armored.accept(self.bullet2)
        self.assertEqual(self.armored.health, 125 - 32)


if __name__ == '__main__':
    unittest.main()
