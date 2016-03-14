import unittest

from katas.kyu_8.grasshopper_terminal_game_1 import Hero


class HeroTestCase(unittest.TestCase):
    def setUp(self):
        self.myHero = Hero()

    def test_equals(self):
        self.assertEqual(self.myHero.name, 'Hero')

    def test_equals_2(self):
        self.assertEqual(self.myHero.experience, 0)

    def test_equals_3(self):
        self.assertEqual(self.myHero.health, 100)

    def test_equals_4(self):
        self.assertEqual(self.myHero.position, '00')

    def test_equals_5(self):
        self.assertEqual(self.myHero.damage, 5)


if __name__ == '__main__':
    unittest.main()
