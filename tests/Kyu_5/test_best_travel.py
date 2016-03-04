import unittest

from Kyu_5.best_travel import choose_best_sum


class BestSumTestCase(unittest.TestCase):
    def setUp(self):
        self.distances = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123,
                          2333, 144, 50, 132, 123, 34, 89]

    def test_equals(self):
        self.assertEqual(choose_best_sum(230, 4, self.distances), 230)

    def test_equals_2(self):
        self.assertEqual(choose_best_sum(430, 5, self.distances), 430)

    def test_none(self):
        self.assertIsNone(choose_best_sum(430, 8, self.distances))


if __name__ == '__main__':
    unittest.main()
