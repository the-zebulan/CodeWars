import unittest

from katas.kyu_6.split_strings import solution


class SplitStringsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(solution('asdfadsf'), ['as', 'df', 'ad', 'sf'])

    def test_equal_2(self):
        self.assertEqual(solution('asdfads'), ['as', 'df', 'ad', 's_'])

    def test_equal_3(self):
        self.assertEqual(solution(''), [])

    def test_equal_4(self):
        self.assertEqual(solution('x'), ['x_'])
