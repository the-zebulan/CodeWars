import unittest

from katas.kyu_7.is_every_value_in_the_array_an_array import arr_check


class ArrCheckTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(arr_check([]))

    def test_true_2(self):
        self.assertTrue(arr_check([['string']]))

    def test_true_3(self):
        self.assertTrue(arr_check([[1], [2], [3]]))

    def test_false_1(self):
        self.assertFalse(arr_check([[], {}]))

    def test_false_2(self):
        self.assertFalse(arr_check(['A', 'R', 'R', 'A', 'Y']))
