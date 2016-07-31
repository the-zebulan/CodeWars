import unittest

from katas.kyu_8.determine_offspring_sex_based_on_genes import chromosoneCheck


class ChromosomeCheckTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(chromosoneCheck('XY'),
                         "Congratulations! You're going to have a son.")

    def test_equal_2(self):
        self.assertEqual(chromosoneCheck('XX'),
                         "Congratulations! You're going to have a daughter.")
