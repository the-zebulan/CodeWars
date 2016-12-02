import unittest

from katas.beta.sorting_integers_into_a_nested_list import group_ints


class GroupIntsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(group_ints([], 0), [])

    def test_equal_2(self):
        self.assertEqual(group_ints([1], 1), [[1]])

    def test_equal_3(self):
        self.assertEqual(group_ints([1, 2, 3], 0), [[1, 2, 3]])

    def test_equal_4(self):
        self.assertEqual(group_ints([1, 2, 3], 3), [[1, 2], [3]])

    def test_equal_5(self):
        self.assertEqual(group_ints(
            [-1, -1, -1, 10, 10, 10, -1, -1, -1, 10, -1, 10], 10),
            [[-1, -1, -1], [10, 10, 10], [-1, -1, -1], [10], [-1], [10]])

    def test_equal_6(self):
        self.assertEqual(group_ints([1, 1, 1, 0, 0, 6, 10, 5, 10], 6),
                         [[1, 1, 1, 0, 0], [6, 10], [5], [10]])
