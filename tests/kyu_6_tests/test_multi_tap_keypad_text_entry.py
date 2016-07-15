import unittest

from katas.kyu_6.multi_tap_keypad_text_entry import presses


class PressesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(presses('LOL'), 9)

    def test_equals_2(self):
        self.assertEqual(presses('HOW R U'), 13)

    def test_equals_3(self):
        self.assertEqual(presses('WHERE DO U WANT 2 MEET L8R'), 47)
