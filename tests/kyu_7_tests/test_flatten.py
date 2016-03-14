import unittest

from katas.kyu_7.flatten import flatten


class FlattenTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_equals_2(self):
        self.assertEqual(flatten([[1, 2, 3], ['a', 'b', 'c'], [1, 2, 3]]),
                         [1, 2, 3, 'a', 'b', 'c', 1, 2, 3])

    def test_equals_3(self):
        self.assertEqual(flatten([[[1, 2, 3]]]), [[1, 2, 3]])


if __name__ == '__main__':
    unittest.main()
