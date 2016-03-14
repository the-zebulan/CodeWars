import unittest

from katas.beta.unique_sum import unique_sum


class UniqueSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(unique_sum([1, 2, 3]), 6)

    def test_equals_2(self):
        self.assertEqual(unique_sum([1, 3, 8, 1, 8]), 12)

    def test_equals_3(self):
        self.assertEqual(unique_sum([-1, -1, 5, 2, -7]), -1)


if __name__ == '__main__':
    unittest.main()
