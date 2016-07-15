# coding=utf-8
import unittest

from katas.kyu_5.ninja_vs_samurai_attack_block import Warrior


class WarriorTestCase(unittest.TestCase):
    def test_equals_1(self):
        ninja = Warrior('Hanzo Hattori')
        samurai = Warrior('Ryōma Sakamoto')
        samurai.block = 'l'
        ninja.attack(samurai, 'h')
        self.assertEqual(samurai.health, 90)

    def test_equals_2(self):
        ninja = Warrior('Hanzo Hattori')
        samurai = Warrior('Ryōma Sakamoto')
        samurai.attack(ninja, 'h')
        self.assertEqual(ninja.health, 85)

    def test_equals_3(self):
        ninja = Warrior('Hanzo Hattori')
        ninja.set_health(0)
        self.assertTrue(ninja.deceased)
        self.assertFalse(ninja.zombie)

    def test_equals_4(self):
        ninja = Warrior('Hanzo Hattori')
        samurai = Warrior('Ryōma Sakamoto')
        samurai.set_health(0)
        ninja.attack(samurai, 'l')
        self.assertTrue(samurai.zombie)
