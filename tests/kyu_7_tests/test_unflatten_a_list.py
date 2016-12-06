import unittest

from katas.kyu_7.unflatten_a_list import unflatten


class UnflattenTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(unflatten([3, 5, 2, 1]), [[3, 5, 2], 1])

    def test_equal_2(self):
        self.assertEqual(unflatten([1, 4, 5, 2, 1, 2, 4, 5, 2, 6, 2, 3, 3]),
                         [1, [4, 5, 2, 1], 2, [4, 5, 2, 6], 2, [3, 3]])

    def test_equal_3(self):
        self.assertEqual(unflatten([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_equal_4(self):
        self.assertEqual(unflatten([1]), [1])

    def test_equal_5(self):
        self.assertEqual(unflatten([99, 1, 1, 1]), [[99, 1, 1, 1]])

    def test_equal_6(self):
        self.assertEqual(unflatten([3, 1, 1, 3, 1, 1]),
                         [[3, 1, 1], [3, 1, 1]])
