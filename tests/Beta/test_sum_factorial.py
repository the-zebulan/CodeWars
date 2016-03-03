import unittest

from Beta.sum_factorial import sum_factorial


class SumFactorialTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_factorial([4, 6]), 744)

    def test_equals_2(self):
        self.assertEqual(sum_factorial([5, 4, 1]), 145)


if __name__ == '__main__':
    unittest.main()
