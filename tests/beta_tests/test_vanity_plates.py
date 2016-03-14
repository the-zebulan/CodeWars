import unittest

from beta.vanity_plates import vanity_plate


class VanityPlateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(vanity_plate('boss'), 'BOSS')

    def test_equals_2(self):
        self.assertEqual(vanity_plate('boss dude'), 'BSS DDE')

    def test_equals_3(self):
        self.assertEqual(vanity_plate('b0ss dude'), 'B0SS DDE')

    def test_equals_4(self):
        self.assertEqual(vanity_plate('the big boss'), 'THEBGBSS')

    def test_equals_5(self):
        self.assertEqual(vanity_plate('the biggest boss around'), 'TBBA')

    def test_equals_6(self):
        self.assertEqual(vanity_plate('a 00000 a'), 'A00000A')


if __name__ == '__main__':
    unittest.main()
