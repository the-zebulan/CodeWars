import unittest

from katas.kyu_8.are_they_opposite import is_opposite


class IsOppositeTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(is_opposite('ab', 'AB'))

    def test_true_2(self):
        self.assertTrue(is_opposite('aB', 'Ab'))

    def test_true_3(self):
        self.assertTrue(is_opposite('aBcd', 'AbCD'))

    def test_false_1(self):
        self.assertFalse(is_opposite('AB', 'Ab'))

    def test_false_2(self):
        self.assertFalse(is_opposite('', ''))
