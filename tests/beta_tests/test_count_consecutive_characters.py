import unittest

from katas.beta.count_consecutive_characters import count_consecutives


class CountConsecutivesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(count_consecutives('a'), '1a')

    def test_equal_2(self):
        self.assertEqual(count_consecutives('aaabbccc'), '3a2b3c')

    def test_equal_3(self):
        self.assertEqual(count_consecutives('annie mommy dummy '),
                         '1a2n1i1e1 1m1o2m1y1 1d1u2m1y1 ')
