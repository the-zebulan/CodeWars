import unittest

from katas.beta.trigrams import trigrams


class TrigramsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(trigrams('the quick red'),
                         'the he_ e_q _qu qui uic ick ck_ k_r _re red')

    def test_equals_2(self):
        self.assertEqual(trigrams('Hi'), '')
