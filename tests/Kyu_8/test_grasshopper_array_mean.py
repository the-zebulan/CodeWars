import unittest

from Kyu_8.grasshopper_array_mean import find_average


class FindAverageTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_average([1]), 1)

    def test_equals_2(self):
        self.assertEqual(find_average([1, 3, 5, 7]), 4)

    def test_equals_3(self):
        self.assertEqual(find_average([-1, 3, 5, -7]), 0)

    def test_equals_4(self):
        self.assertEqual(find_average([5, 7, 3, 7]), 5.5)

    def test_equals_5(self):
        self.assertEqual(find_average([]), 0)


if __name__ == '__main__':
    unittest.main()
