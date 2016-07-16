import unittest

from katas.beta.vanity_plates import vanity_plate


class VanityPlateTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(vanity_plate('boss'), 'BOSS')

    def test_equal_2(self):
        self.assertEqual(vanity_plate('boss dude'), 'BSS DDE')

    def test_equal_3(self):
        self.assertEqual(vanity_plate('b0ss dude'), 'B0SS DDE')

    def test_equal_4(self):
        self.assertEqual(vanity_plate('the big boss'), 'THEBGBSS')

    def test_equal_5(self):
        self.assertEqual(vanity_plate('the biggest boss around'), 'TBBA')

    def test_equal_6(self):
        self.assertEqual(vanity_plate('a 00000 a'), 'A00000A')

    def test_equal_7(self):
        self.assertEqual(vanity_plate('1 2 3 4 5 6 7 8 9 0'), '')
