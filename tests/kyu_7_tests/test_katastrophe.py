import unittest

from katas.kyu_7.katastrophe import strong_enough


class StrongEnoughTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(strong_enough(
            [[2, 3, 1], [3, 1, 1], [1, 1, 2]], 2), 'Safe!')

    def test_equals_2(self):
        self.assertEqual(strong_enough(
            [[5, 8, 7], [3, 3, 1], [4, 1, 2]], 2), 'Safe!')

    def test_equals_3(self):
        self.assertEqual(strong_enough(
            [[5, 8, 7], [3, 3, 1], [4, 1, 2]], 3), 'Needs Reinforcement!')


if __name__ == '__main__':
    unittest.main()
