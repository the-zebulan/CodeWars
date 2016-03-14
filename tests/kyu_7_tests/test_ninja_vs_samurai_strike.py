import unittest

from katas.kyu_7.ninja_vs_samurai_strike import Warrior


class WarriorTestCase(unittest.TestCase):
    def setUp(self):
        self.ninja = Warrior('Ninja')
        self.samurai = Warrior('Samurai')

    def test_equals(self):
        self.samurai.strike(self.ninja, 3)
        self.assertEqual(self.ninja.health, 70)


if __name__ == '__main__':
    unittest.main()
