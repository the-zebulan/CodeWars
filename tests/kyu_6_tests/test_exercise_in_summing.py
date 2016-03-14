import unittest

from Kyu_6.exercise_in_summing import maximum_sum, minimum_sum


class ExerciseInSummingTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(minimum_sum([5, 4, 3, 2, 1], 2), 3)

    def test_equals_2(self):
        self.assertEqual(maximum_sum([5, 4, 3, 2, 1], 3), 12)

    def test_equals_3(self):
        self.assertEqual(minimum_sum([5, 4, 3, 2, 1], 7), 15)

    def test_equals_4(self):
        self.assertEqual(minimum_sum([], 3), 0)


if __name__ == '__main__':
    unittest.main()
