import unittest

from katas.kyu_8.are_they_opposite import isOpposite


class IsOppositeTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(isOpposite('ab', 'AB'))

    def test_true_2(self):
        self.assertTrue(isOpposite('aB', 'Ab'))

    def test_true_3(self):
        self.assertTrue(isOpposite('aBcd', 'AbCD'))

    def test_false_1(self):
        self.assertFalse(isOpposite('AB', 'Ab'))

    def test_false_2(self):
        self.assertFalse(isOpposite('', ''))
