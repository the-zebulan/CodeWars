import unittest

from katas.beta.logistic_map import logistic_map


class LogisticMapTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(logistic_map(3, 3, [0], [0]),
                         [[0, 1, 2], [1, 2, 3], [2, 3, 4]])

    def test_equal_2(self):
        self.assertEqual(logistic_map(3, 3, [2], [2]),
                         [[4, 3, 2], [3, 2, 1], [2, 1, 0]])

    def test_equal_3(self):
        self.assertEqual(logistic_map(1, 1, [0], [0]), [[0]])

    def test_equal_4(self):
        self.assertEqual(logistic_map(5, 2, [0, 4], [0, 0]),
                         [[0, 1, 2, 1, 0], [1, 2, 3, 2, 1]])

    def test_equal_5(self):
        self.assertEqual(logistic_map(2, 2, [], []),
                         [[None, None], [None, None]])


if __name__ == '__main__':
    unittest.main()
