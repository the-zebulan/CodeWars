import unittest

from katas.beta.spy_games_rebuild_your_decoder import decrypt


class RebuildYourDecoderTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(decrypt('x20*6<xY y875_r97L'), 'hi')

    def test_equal_2(self):
        self.assertEqual(decrypt('8S6 K00= 3Ob28W4'), 'n q')
