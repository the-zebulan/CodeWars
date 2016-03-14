import unittest

from katas.kyu_8.get_the_mean_of_array import get_average


class GetAverageTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_average([2, 2, 2, 2]), 2)

    def test_equals_2(self):
        self.assertEqual(get_average([1, 5, 87, 45, 8, 8]), 25)

    def test_equals_3(self):
        self.assertEqual(get_average([2, 5, 13, 20, 16, 16, 10]), 11)

    def test_equals_4(self):
        self.assertEqual(get_average(
            [1, 2, 15, 15, 17, 11, 12, 17, 17, 14, 13, 15, 6, 11, 8, 7]), 11)


if __name__ == '__main__':
    unittest.main()
