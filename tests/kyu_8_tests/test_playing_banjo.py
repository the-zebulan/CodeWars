import unittest

from kyu_8.playing_banjo import areYouPlayingBanjo


class BanjoTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(areYouPlayingBanjo('martin'),
                         'martin does not play banjo')

    def test_equals_2(self):
        self.assertEqual(areYouPlayingBanjo('Rikke'), 'Rikke plays banjo')


if __name__ == '__main__':
    unittest.main()
