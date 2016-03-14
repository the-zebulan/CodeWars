import unittest

from beta.nested_list_depth import list_depth


class ListDepthTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(list_depth([True]), 1)

    def test_equals_2(self):
        self.assertEqual(list_depth([]), 1)

    def test_equals_3(self):
        self.assertEqual(list_depth([2, 'yes', [True, False]]), 2)

    def test_equals_4(self):
        self.assertEqual(list_depth(
            [1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1]), 6)

    def test_equals_5(self):
        self.assertEqual(list_depth(
            [2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]]), 2)


if __name__ == '__main__':
    unittest.main()
