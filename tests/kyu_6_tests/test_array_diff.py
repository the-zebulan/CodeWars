import unittest

from katas.kyu_6.array_diff import array_diff


class ArrayDiffTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(array_diff([1, 2], [1]), [2])

    def test_equals_2(self):
        self.assertEqual(array_diff([1, 2, 2], [1]), [2, 2])

    def test_equals_3(self):
        self.assertEqual(array_diff([1, 2, 2], [2]), [1])

    def test_equals_4(self):
        self.assertEqual(array_diff([1, 2, 2], []), [1, 2, 2])

    def test_equals_5(self):
        self.assertEqual(array_diff([], [1, 2]), [])


if __name__ == '__main__':
    unittest.main()
