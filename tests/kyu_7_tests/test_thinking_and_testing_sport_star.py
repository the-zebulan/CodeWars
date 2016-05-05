import unittest

from katas.kyu_7.thinking_and_testing_sport_star import testit as solution


class SportStarTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(solution(
            ['run', 'jump', 'run', 'jump', 'run'], '_|_|_'
        ), '_|_|_')

    def test_equal_2(self):
        self.assertEqual(solution(
            ['run', 'jump', 'run', 'run', 'run'], '_|_|_'
        ), '_|_/_')

    def test_equal_3(self):
        self.assertEqual(solution(
            ['run', 'run', 'run', 'run', 'run'], '_|_|_'
        ), '_/_/_')

    def test_equal_4(self):
        self.assertEqual(solution(
            ['jump', 'jump', 'jump', 'jump', 'jump'], '_|_|_'
        ), 'x|x|x')

    def test_equal_5(self):
        self.assertEqual(solution(
            ['jump', 'run', 'jump', 'run', 'jump'], '_|_|_'
        ), 'x/x/x')


if __name__ == '__main__':
    unittest.main()
