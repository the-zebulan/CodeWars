import unittest

from Kyu_7.sum_of_all_arguments import sum_args


class SumArgsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_args(1, 2, 3), 6)

    def test_equals_2(self):
        self.assertEqual(sum_args(8, 2), 10)

    def test_equals_3(self):
        self.assertEqual(sum_args(1, 2, 3, 4, 5), 15)


if __name__ == '__main__':
    unittest.main()
