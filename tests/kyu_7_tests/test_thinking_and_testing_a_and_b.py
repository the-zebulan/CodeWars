import unittest

from katas.kyu_7.thinking_and_testing_a_and_b import testit as solution


class TestItTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(0, 1), 1)

    def test_equals_2(self):
        self.assertEqual(solution(1, 2), 3)

    def test_equals_3(self):
        self.assertEqual(solution(10, 20), 30)

    def test_equals_4(self):
        self.assertEqual(solution(1, 1), 1)

    def test_equals_5(self):
        self.assertEqual(solution(1, 3), 3)
