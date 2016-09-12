import unittest

from katas.beta.rammstein_needs_your_help import feuer_frei


class FeuerFreiTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(feuer_frei(5, 20), 'Perfekt!')

    def test_equal_2(self):
        self.assertEqual(feuer_frei(5, 200), 900)

    def test_equal_3(self):
        self.assertEqual(feuer_frei(5, 2),
                         '90 Stunden mehr Benzin ben\xf6tigt.')
