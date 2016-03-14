import unittest

from katas.kyu_6.rotate_array import rotate


class RotateTestCase(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]

    def test_equals(self):
        self.assertEqual(rotate(self.data, 1), [5, 1, 2, 3, 4])

    def test_equals_2(self):
        self.assertEqual(rotate(self.data, 2), [4, 5, 1, 2, 3])

    def test_equals_3(self):
        self.assertEqual(rotate(self.data, 3), [3, 4, 5, 1, 2])

    def test_equals_4(self):
        self.assertEqual(rotate(self.data, 4), [2, 3, 4, 5, 1])

    def test_equals_5(self):
        self.assertEqual(rotate(self.data, 5), [1, 2, 3, 4, 5])

    def test_equals_6(self):
        self.assertEqual(rotate(self.data, 0), [1, 2, 3, 4, 5])

    def test_equals_7(self):
        self.assertEqual(rotate(self.data, -1), [2, 3, 4, 5, 1])

    def test_equals_8(self):
        self.assertEqual(rotate(self.data, -2), [3, 4, 5, 1, 2])

    def test_equals_9(self):
        self.assertEqual(rotate(self.data, -3), [4, 5, 1, 2, 3])

    def test_equals_10(self):
        self.assertEqual(rotate(self.data, -4), [5, 1, 2, 3, 4])

    def test_equals_11(self):
        self.assertEqual(rotate(self.data, -5), [1, 2, 3, 4, 5])

    def test_equals_12(self):
        self.assertEqual(rotate(self.data, 7), [4, 5, 1, 2, 3])

    def test_equals_13(self):
        self.assertEqual(rotate(self.data, 11), [5, 1, 2, 3, 4])

    def test_equals_14(self):
        self.assertEqual(rotate(self.data, 12478), [3, 4, 5, 1, 2])

    def test_equals_15(self):
        self.assertEqual(rotate(['a', 'b', 'c'], 1), ['c', 'a', 'b'])

    def test_equals_16(self):
        self.assertEqual(rotate([1.0, 2.0, 3.0], 1), [3.0, 1.0, 2.0])

    def test_equals_17(self):
        self.assertEqual(rotate([True, True, False], 1), [False, True, True])


if __name__ == '__main__':
    unittest.main()
