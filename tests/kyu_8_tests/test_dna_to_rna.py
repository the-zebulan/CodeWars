import unittest

from kyu_8.dna_to_rna import DNAtoRNA


class DNAToRNATestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(DNAtoRNA('TTTT'), 'UUUU')

    def test_equals_2(self):
        self.assertEqual(DNAtoRNA('GCAT'), 'GCAU')

    def test_equals_3(self):
        self.assertEqual(DNAtoRNA('GACCGCCGCC'), 'GACCGCCGCC')


if __name__ == '__main__':
    unittest.main()
