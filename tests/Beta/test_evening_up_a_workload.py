import unittest

from Beta.evening_up_a_workload import split_workload


class SplitWorkloadTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(split_workload([1, 6, 2, 3, 5, 4, 1]), (4, 2))

    def test_equals_2(self):
        self.assertEqual(split_workload([]), (None, None))


if __name__ == '__main__':
    unittest.main()
