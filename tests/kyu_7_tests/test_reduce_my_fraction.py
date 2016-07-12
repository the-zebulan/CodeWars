import unittest

from katas.kyu_7.reduce_my_fraction import reduce as solution


class ReduceMyFractionTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(solution([60, 20]), [3, 1])

    def test_equal_2(self):
        self.assertEqual(solution([80, 120]), [2, 3])

    def test_equal_3(self):
        self.assertEqual(solution([4, 2]), [2, 1])

    def test_equal_4(self):
        self.assertEqual(solution([45, 120]), [3, 8])

    def test_equal_5(self):
        self.assertEqual(solution([1000, 1]), [1000, 1])

    def test_equal_6(self):
        self.assertEqual(solution([1, 1]), [1, 1])


if __name__ == '__main__':
    unittest.main()
