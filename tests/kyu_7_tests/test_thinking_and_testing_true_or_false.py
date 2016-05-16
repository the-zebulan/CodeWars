import unittest

from katas.kyu_7.thinking_and_testing_true_or_false import testit as solution


class ThinkingAndTestingTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(0), 0)

    def test_equals_2(self):
        self.assertEqual(solution(2), 1)

    def test_equals_3(self):
        self.assertEqual(solution(3), 2)

    def test_equals_4(self):
        self.assertEqual(solution(4), 1)

    def test_equals_5(self):
        self.assertEqual(solution(5), 2)

    def test_equals_6(self):
        self.assertEqual(solution(6), 2)

    def test_equals_7(self):
        self.assertEqual(solution(7), 3)

    def test_equals_8(self):
        self.assertEqual(solution(8), 1)

    def test_equals_9(self):
        self.assertEqual(solution(9), 2)

    def test_equals_10(self):
        self.assertEqual(solution(10), 2)

    def test_equals_11(self):
        self.assertEqual(solution(100), 3)

    def test_equals_12(self):
        self.assertEqual(solution(1000), 6)

    def test_equals_13(self):
        self.assertEqual(solution(10000), 5)


if __name__ == '__main__':
    unittest.main()
