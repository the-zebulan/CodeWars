import unittest

from katas.kyu_6.checking_groups import group_check


class CheckingGroupsTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(group_check('({})'))

    def test_true_2(self):
        self.assertTrue(group_check('[[]()]'))

    def test_true_3(self):
        self.assertTrue(group_check('[{()}]'))

    def test_true_4(self):
        self.assertTrue(group_check('()'))

    def test_false_1(self):
        self.assertFalse(group_check('{(})'))

    def test_false_2(self):
        self.assertFalse(group_check('([]'))

    def test_false_3(self):
        self.assertFalse(group_check('[])'))

    def test_false_4(self):
        self.assertFalse(group_check('({'))
