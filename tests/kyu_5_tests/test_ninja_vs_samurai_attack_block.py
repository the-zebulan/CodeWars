# coding=utf-8
import unittest

from katas.kyu_5.ninja_vs_samurai_attack_block import Warrior


class WarriorTestCase(unittest.TestCase):
    def setUp(self):
        self.ninja = Warrior('Hanzo Hattori')
        self.samurai = Warrior('Ryōma Sakamoto')

    def test_equals(self):
        self.samurai.block = 'l'
        self.ninja.attack(self.samurai, 'h')
        self.assertEqual(self.samurai.health, 90)
