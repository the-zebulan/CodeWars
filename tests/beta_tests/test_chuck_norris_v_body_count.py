import unittest

from katas.beta.chuck_norris_v_body_count import body_count


class BodyCountTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(body_count('A6C2E5Z9A4.-F%8.08.'))

    def test_true_2(self):
        self.assertTrue(body_count('PP P6A6T5F5S3.-Z%1.11.hgr'))

    def test_true_3(self):
        self.assertTrue(body_count('A6A1E3A8M2.-Q%8.88.'))

    def test_true_4(self):
        self.assertTrue(body_count('d G8H1E2O9N3.-W%8.56. f'))

    def test_true_5(self):
        self.assertTrue(body_count('B4A1D1I8B4.-E%8.76.'))

    def test_true_6(self):
        self.assertTrue(body_count('ffr65A C8K4D9U7V5.-Y%8.00.'))

    def test_true_7(self):
        self.assertTrue(body_count(' 76     B2L4D0A8C6.-T%8.90.       lkd'))

    def test_false_1(self):
        self.assertFalse(body_count('B2L4D0A8C6.-T%8.90'))

    def test_false_2(self):
        self.assertFalse(body_count('B2L4D0AFC6.-T%8.90.'))

    def test_false_3(self):
        self.assertFalse(body_count('B4A1D1I8B4'))

    def test_false_4(self):
        self.assertFalse(body_count('B4A6666...'))

    def test_false_5(self):
        self.assertFalse(body_count('B4A1D1I000.-E%0.00.)'))

    def test_false_6(self):
        self.assertFalse(body_count('.-E%8.76.'))

    def test_false_7(self):
        self.assertFalse(body_count('B4A1t6I7.-E%8.76.'))

    def test_false_8(self):
        self.assertFalse(body_count('b4A1D1I8B4.-E%8.76.'))
