import unittest

from katas.kyu_6.sum_consecutives import sum_consecutives


class SumConsecutivesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_consecutives([1, 4, 4, 4, 0, 4, 3, 3, 1]),
                         [1, 12, 0, 4, 6, 1])

    def test_equals_2(self):
        self.assertEqual(sum_consecutives([1, 1, 7, 7, 3]), [2, 14, 3])

    def test_equals_3(self):
        self.assertEqual(sum_consecutives([-5, -5, 7, 7, 12, 0]),
                         [-10, 14, 12, 0])

    def test_equals_4(self):
        self.assertEqual(sum_consecutives([3, 3, 3, 3, 1]), [12, 1])


if __name__ == '__main__':
    unittest.main()
