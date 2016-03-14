import unittest

from katas.kyu_6.same_array import same


class SameTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(same([], []))

    def test_true_2(self):
        self.assertTrue(same([[2, 5], [3, 6]], [[5, 2], [3, 6]]))

    def test_true_3(self):
        self.assertTrue(same([[2, 5], [3, 6]], [[6, 3], [5, 2]]))

    def test_true_4(self):
        self.assertTrue(same([[2, 5], [3, 6]], [[6, 3], [2, 5]]))

    def test_true_5(self):
        self.assertTrue(same(
            [[2, 5], [3, 5], [6, 2]], [[2, 6], [5, 3], [2, 5]]))

    def test_true_6(self):
        self.assertTrue(same(
            [[2, 5], [3, 5], [6, 2]], [[3, 5], [6, 2], [5, 2]]))

    def test_false(self):
        self.assertFalse(same([[2, 3], [3, 4]], [[4, 3], [2, 4]]))

    def test_false_2(self):
        self.assertFalse(same([[2, 3], [3, 2]], [[2, 3]]))


if __name__ == '__main__':
    unittest.main()
