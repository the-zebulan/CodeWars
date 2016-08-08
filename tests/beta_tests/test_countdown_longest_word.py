import unittest

from katas.beta.countdown_longest_word import longest_word


class LongestWordTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(longest_word('GQEMAUVXY'), ['GAME'])

    def test_equal_2(self):
        self.assertEqual(longest_word('TDWAYZROE'),
                         ['TODAY', 'TOWER', 'TRADE', 'WATER'])

    def test_equal_3(self):
        self.assertEqual(longest_word('EAEEAYITB'), ['BEAT', 'BITE', 'BYTE'])

    def test_equal_4(self):
        self.assertEqual(longest_word('AKUIYOOLO'), ['LOOK', 'YOLK'])

    def test_equal_5(self):
        self.assertEqual(longest_word('GVDTCAESU'),
                         ['CAGES', 'CAUSE', 'CAVES', 'DATES', 'GATES',
                          'GUEST', 'STAGE', 'USAGE'])

    def test_is_none_1(self):
        self.assertIsNone(longest_word(''))

    def test_is_none_2(self):
        self.assertIsNone(longest_word('MKMKMKMKM'))

    def test_is_none_3(self):
        self.assertIsNone(longest_word('IIIWUGEZI'))
