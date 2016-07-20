import unittest

from katas.kyu_7.compare_strings_by_sum_of_chars import compare


class CompareStringsTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(compare('AD', 'BC'))

    def test_true_2(self):
        self.assertTrue(compare('gf', 'FG'))

    def test_true_3(self):
        self.assertTrue(compare('zz1', ''))

    def test_true_4(self):
        self.assertTrue(compare('ZzZz', 'ffPFF'))

    def test_true_5(self):
        self.assertTrue(compare(None, ''))

    def test_true_6(self):
        self.assertTrue(compare('!!', '7476'))

    def test_true_7(self):
        self.assertTrue(compare('##', '1176'))

    def test_false_1(self):
        self.assertFalse(compare('AD', 'DD'))

    def test_false_2(self):
        self.assertFalse(compare('Ad', 'DD'))

    def test_false_3(self):
        self.assertFalse(compare('kl', 'lz'))
