import unittest

from katas.kyu_6.multiples_of_3_and_5 import solution


class MultiplesOfThreeAndFiveTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(10), 23)

    def test_equals_2(self):
        self.assertEqual(solution(100), 2318)

    def test_equals_3(self):
        self.assertEqual(solution(997), 232169)
