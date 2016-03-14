import unittest

from kyu_8.player_rank_up import playerRankUp


class PlayerRankUpTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(playerRankUp(180),
                         'Well done! You have advanced to the qualifying sta'
                         'ge. Win 2 out of your next 3 games to rank up.')

    def test_false(self):
        self.assertFalse(playerRankUp(64))


if __name__ == '__main__':
    unittest.main()
