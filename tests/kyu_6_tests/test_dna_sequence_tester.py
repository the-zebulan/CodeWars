import unittest

from katas.kyu_6.dna_sequence_tester import check_DNA


class CheckDNATestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_DNA('ATGCTACG', 'CGTAGCAT'))

    def test_true_2(self):
        self.assertTrue(check_DNA('AGTCTGTATGCATCGTACCC',
                                  'GGGTACGATGCATACAGACT'))

    def test_true_3(self):
        self.assertTrue(check_DNA('GCGCTGCTAGCTGATCGA',
                                  'ACGTACGATCGATCAGCTAGCAGCGCTAC'))

    def test_true_4(self):
        self.assertTrue(check_DNA('GCTAGCACCCATTAGGAGATAC', 'CTCCTAATGGGTG'))

    def test_true_5(self):
        self.assertTrue(check_DNA('TAGCATCGCCAAATTATGCGTCAGTCTGCCCG',
                                  'GGGCA'))

    def test_true_6(self):
        self.assertTrue(check_DNA('TGCTACGTACGATCGACGATCCACGAC',
                                  'GTCGTGGATCGTCGATCGTACGTAGCA'))

    def test_false(self):
        self.assertFalse(check_DNA('GTCTTAGTGTAGCTATGCATGC',
                                   'GCATGCATAGCTACACTACGAC'))

    def test_false_2(self):
        self.assertFalse(check_DNA('ATGCCTACGGCCATATATATTTAG',
                                   'CTAAATATGTATGGCCGTAGGCAT'))

    def test_false_3(self):
        self.assertFalse(check_DNA('GTCACCGA', 'TCGGCTGAC'))

    def test_false_4(self):
        self.assertFalse(check_DNA('TAATACCCGACTAATTCCCC',
                                   'GGGGAATTTCGGGTATTA'))

    def test_false_5(self):
        self.assertFalse(check_DNA('GCTAACTCGAAGCTATACGTTA',
                                   'TAACGTATAGCTTCGAGGTTAGC'))

    def test_false_6(self):
        self.assertFalse(check_DNA('ACGACTACGTGCGCCGCTAATATT', 'GCACGGGTCGT'))

    def test_false_7(self):
        self.assertFalse(check_DNA('CGATACGAACCCATAATCG',
                                   'CTACACCGGCCGATTATGG'))

    def test_false_8(self):
        self.assertFalse(check_DNA('CGACATCGAGGGGGCTCAGAAGTACTGA',
                                   'CATGGCGTCAGTACTTCTGAGCC'))

    def test_false_9(self):
        self.assertFalse(check_DNA('GAGCAGTTGGTAGTTT', 'GTATCGAAACTACCA'))

    def test_false_10(self):
        self.assertFalse(check_DNA('TACGATCCAAGGCTACTCAGAG',
                                   'GGGATACTCTGAGTAGCCTTGGAA'))

    def test_false_11(self):
        self.assertFalse(check_DNA('ATGCTACG', 'CGTAGCAA'))


if __name__ == '__main__':
    unittest.main()
