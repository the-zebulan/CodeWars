import unittest

from katas.kyu_6.playing_with_passphrases import play_pass


class PlayingWithPassphrasesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(play_pass('I LOVE YOU!!!', 1), '!!!vPz fWpM J')

    def test_equals_2(self):
        self.assertEqual(play_pass(
            'MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015', 2),
            '4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO')
