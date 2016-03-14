import unittest

from katas.kyu_7.complementary_dna import DNA_strand


class DNAStrandTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(DNA_strand('AAAA'), 'TTTT')

    def test_equals_2(self):
        self.assertEqual(DNA_strand('ATTGC'), 'TAACG')

    def test_equals_3(self):
        self.assertEqual(DNA_strand('GTAT'), 'CATA')


if __name__ == '__main__':
    unittest.main()
