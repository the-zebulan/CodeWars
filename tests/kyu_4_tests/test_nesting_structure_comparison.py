import unittest

from katas.kyu_4.nesting_structure_comparison import same_structure_as


class SameStructureAsTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(same_structure_as([1, 1, 1], [2, 2, 2]))

    def test_true_2(self):
        self.assertTrue(same_structure_as([1, [1, 1]], [2, [2, 2]]))

    def test_true_3(self):
        self.assertTrue(same_structure_as([[[], []]], [[[], []]]))

    def test_false_1(self):
        self.assertFalse(same_structure_as([1, [1, 1]], [[2, 2], 2]))

    def test_false_2(self):
        self.assertFalse(same_structure_as([1, [1, 1]], [[2], 2]))

    def test_false_3(self):
        self.assertFalse(same_structure_as([[[], []]], [[1, 1]]))
