import unittest

from beta.transpose_of_a_matrix import transpose


class TransposeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(transpose([]), [])

    def test_equals_2(self):
        self.assertEqual(transpose([[1]]), [[1]])

    def test_equals_3(self):
        self.assertEqual(transpose([[0, 1]]), [[0], [1]])

    def test_equals_4(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]),
                         [[1, 4], [2, 5], [3, 6]])

    def test_equals_5(self):
        self.assertEqual(transpose([[]]), [[]])

    def test_equals_6(self):
        self.assertEqual(transpose([[], [], [], [], [], []]), [[]])


if __name__ == '__main__':
    unittest.main()
