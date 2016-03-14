import unittest

from katas.kyu_7.unlimited_sum import sum


class UnlimitedSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum(1, 2, 3), 6)

    def test_equals_2(self):
        self.assertEqual(sum('1', 1, '2', 2), 3)


if __name__ == '__main__':
    unittest.main()
