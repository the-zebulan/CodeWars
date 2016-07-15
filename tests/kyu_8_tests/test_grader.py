import unittest

from katas.kyu_8.grader import grader


class GraderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(grader(0.7), 'C')

    def test_equals_2(self):
        self.assertEqual(grader(0.9), 'A')

    def test_equals_3(self):
        self.assertEqual(grader(0.6), 'D')

    def test_equals_4(self):
        self.assertEqual(grader(-1), 'F')
