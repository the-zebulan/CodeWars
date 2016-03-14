import unittest

from katas.kyu_7.what_dominates_your_array import dominator


class DominatorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(dominator([3, 4, 3, 2, 3, 1, 3, 3]), 3)

    def test_equals_2(self):
        self.assertEqual(dominator([1, 2, 3, 4, 5]), -1)

    def test_equals_3(self):
        self.assertEqual(dominator([1, 1, 1, 2, 2, 2]), -1)

    def test_equals_4(self):
        self.assertEqual(dominator([1, 1, 1, 2, 2, 2, 2]), 2)

    def test_equals_5(self):
        self.assertEqual(dominator([]), -1)


if __name__ == '__main__':
    unittest.main()
