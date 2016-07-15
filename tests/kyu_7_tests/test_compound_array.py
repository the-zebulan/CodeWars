import unittest

from katas.kyu_7.compound_array import compound_array


class CompoundArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(compound_array([1, 2, 3, 4, 5, 6], [9, 8, 7, 6]),
                         [1, 9, 2, 8, 3, 7, 4, 6, 5, 6])

    def test_equals_2(self):
        self.assertEqual(compound_array(
            [0, 1, 2], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        ), [0, 9, 1, 8, 2, 7, 6, 5, 4, 3, 2, 1, 0])
