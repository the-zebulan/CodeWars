import unittest

from katas.kyu_8.strive_matching_1 import match


class StriveMatchTestCase(unittest.TestCase):
    def setUp(self):
        self.candidate1 = {'min_salary': 120000}
        self.candidate2 = {'min_salary': 190000}
        self.job1 = {'max_salary': 130000}
        self.job2 = {'max_salary': 80000}
        self.job3 = {'max_salary': 171000}

    def test_true(self):
        self.assertTrue(match(self.candidate1, self.job1))

    def test_true_2(self):
        self.assertTrue(match(self.candidate1, self.job3))

    def test_true_3(self):
        self.assertTrue(match(self.candidate2, self.job3))

    def test_false(self):
        self.assertFalse(match(self.candidate1, self.job2))

    def test_false_2(self):
        self.assertFalse(match(self.candidate2, self.job1))

    def test_false_3(self):
        self.assertFalse(match(self.candidate2, self.job2))
