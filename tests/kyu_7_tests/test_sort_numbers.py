import unittest

from katas.kyu_7.sort_numbers import solution


class SortNumbersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution([1, 2, 10, 5]), [1, 2, 5, 10])

    def test_equals_2(self):
        self.assertEqual(solution((1, 2, 10, 5)), [1, 2, 5, 10])


if __name__ == '__main__':
    unittest.main()
