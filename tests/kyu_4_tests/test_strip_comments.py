# coding=utf-8
import unittest

from katas.kyu_4.strip_comments import solution


class StripCommentsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(
            'apples, pears # and bananas\ngrapes\nbananas !apples',
            ['#', '!']), 'apples, pears\ngrapes\nbananas')

    def test_equals_2(self):
        self.assertEqual(solution('#', ['#', '!']), '')

    def test_equals_3(self):
        self.assertEqual(solution('\n§', ['#', '\xc2\xa7']), '\n')
