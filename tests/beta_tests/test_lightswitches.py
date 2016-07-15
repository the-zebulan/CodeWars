import unittest

from katas.beta.lightswitches import lightswitch


class LightswitchTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(lightswitch(3), 1)

    def test_equals_2(self):
        self.assertEqual(lightswitch(4), 2)
