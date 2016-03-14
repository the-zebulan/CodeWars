import unittest

from katas.kyu_7.scoring_tests import score_test


class ScoreTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(score_test([0, 0, 0, 0, 2, 1, 0], 2, 0, 1), 9)

    def test_equals_2(self):
        self.assertEqual(score_test(
            [0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2), 3)


if __name__ == '__main__':
    unittest.main()
