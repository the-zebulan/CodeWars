import unittest

from katas.kyu_6.drunk_friend import decode


class DrunkFriendTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(decode('yvvi'), 'beer')

    def test_equals_2(self):
        self.assertEqual(decode('Blf zoivzwb szw 10 yvvih'),
                         'You already had 10 beers')

    def test_equals_3(self):
        self.assertEqual(decode('Ovg\'h hdrn rm gsv ulfmgzrm!'),
                         'Let\'s swim in the fountain!')

    def test_equals_4(self):
        self.assertEqual(decode('Tl slnv, blf\'iv wifmp'),
                         'Go home, you\'re drunk')
