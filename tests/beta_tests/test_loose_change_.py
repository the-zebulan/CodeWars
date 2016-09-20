import unittest

from katas.beta.loose_change_ import change_count


class ChangeCountTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(change_count('dime penny dollar'), '$1.11')

    def test_equal_2(self):
        self.assertEqual(change_count('dime penny nickel'), '$0.16')

    def test_equal_3(self):
        self.assertEqual(change_count('quarter quarter'), '$0.50')

    def test_equal_4(self):
        self.assertEqual(change_count('dollar penny dollar'), '$2.01')

    def test_equal_5(self):
        self.assertEqual(change_count(
            'dollar dollar dollar dollar dollar dollar dollar dollar dollar'
            ' dollar penny'), '$10.01'
        )
