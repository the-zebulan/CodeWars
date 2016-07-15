import unittest

from katas.kyu_7.dna_gc_content import gc_content


class DnaGcContentTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(gc_content(''), 0.0)

    def test_equal_2(self):
        self.assertEqual(gc_content('A'), 0.0)

    def test_equal_3(self):
        self.assertEqual(gc_content('C'), 100.0)

    def test_equal_4(self):
        self.assertEqual(gc_content('CA'), 50.0)

    def test_equal_5(self):
        self.assertEqual(gc_content('ACTGACTGAACCA'), 46.15)
