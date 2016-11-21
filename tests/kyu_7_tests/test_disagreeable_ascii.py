import unittest

from katas.kyu_7.disagreeable_ascii import get_weight


class GetWeightTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_weight('Joe'), 254)

    def test_equal_2(self):
        self.assertEqual(get_weight('CJ'), 205)

    def test_equal_3(self):
        self.assertEqual(get_weight('cj'), 141)
