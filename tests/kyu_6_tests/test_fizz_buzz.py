import unittest

from kyu_6.fizz_buzz import solution


class FizzBuzzTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(20), [5, 2, 1])

    def test_equals_2(self):
        self.assertEqual(solution(2), [0, 0, 0])

    def test_equals_3(self):
        self.assertEqual(solution(30), [8, 4, 1])

    def test_equals_4(self):
        self.assertEqual(solution(300), [80, 40, 19])


if __name__ == '__main__':
    unittest.main()
