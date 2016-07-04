import unittest

from katas.kyu_7.find_the_motif_in_dna_sequence import motif_locator


class MotifLocatorTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(motif_locator('ACGTGGGGACTAGGGG', 'GGGG'), [5, 13])

    def test_equal_2(self):
        self.assertEqual(motif_locator('ACCGTACCAAGGGACC', 'AAT'), [])

    def test_equal_3(self):
        self.assertEqual(motif_locator('GGG', 'GG'), [1, 2])

    def test_equal_4(self):
        self.assertEqual(motif_locator('TTCCGGAACC', 'CC'), [3, 9])

    def test_equal_5(self):
        self.assertEqual(motif_locator('ACGTTACAACGTTAG', 'ACGT'), [1, 9])

    def test_equal_6(self):
        self.assertEqual(motif_locator('ACGTACGTACGT', 'AAA'), [])

    def test_equal_7(self):
        self.assertEqual(motif_locator('ACGT', 'ACGTGAC'), [])


if __name__ == '__main__':
    unittest.main()
