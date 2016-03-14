import unittest

from Kyu_8.sum_arrays import sum_array


class SumArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_array([]), 0)

    def test_equals_2(self):
        self.assertEqual(sum_array([1, 2, 3]), 6)

    def test_equals_3(self):
        self.assertEqual(sum_array([1.1, 2.2, 3.3]), 6.6)

    def test_equals_4(self):
        self.assertEqual(sum_array([4, 5, 6]), 15)


if __name__ == '__main__':
    unittest.main()
