import unittest

from katas.kyu_6.round_by_half_steps import solution


class RoundByHalfStepsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(4.2), 4)

    def test_equals_2(self):
        self.assertEqual(solution(4.25), 4.5)

    def test_equals_3(self):
        self.assertEqual(solution(4.4), 4.5)

    def test_equals_4(self):
        self.assertEqual(solution(4.6), 4.5)

    def test_equals_5(self):
        self.assertEqual(solution(4.75), 5)

    def test_equals_6(self):
        self.assertEqual(solution(4.8), 5)
