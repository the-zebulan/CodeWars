import unittest

from katas.kyu_7.coding_3_min_a_b_c import find_a_b


class FindABTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(find_a_b([1, 2, 3], 3), [1, 3])

    def test_equal_2(self):
        self.assertEqual(find_a_b([1, 2, 3], 6), [2, 3])

    def test_equal_3(self):
        self.assertEqual(find_a_b([1, 2, 3, 6], 6), [1, 6])

    def test_equal_4(self):
        self.assertEqual(find_a_b([1, 2, 3, 4, 5, 6], 15), [3, 5])

    def test_equal_5(self):
        self.assertEqual(find_a_b([0, 0, 2, 2], 4), [2, 2])

    def test_equal_6(self):
        self.assertEqual(
            find_a_b([-3, -2, -2, -1, 0, 1, 2, 3, 4], 4), [-2, -2]
        )

    def test_equal_7(self):
        self.assertEqual(
            find_a_b([-3, -2, -2, -1, 0, 1, 2, 3, 4], 0), [-3, 0]
        )

    def test_equal_8(self):
        self.assertEqual(find_a_b([-3, -2, -1, 0, 1, 2, 3, 4], 4), [1, 4])

    def test_is_none_1(self):
        self.assertIsNone(find_a_b([1, 2, 3], 7))

    def test_is_none_2(self):
        self.assertIsNone(find_a_b([0, 0, 2], 4))
