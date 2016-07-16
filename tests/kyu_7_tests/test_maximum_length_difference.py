import unittest

from katas.kyu_7.maximum_length_difference import mxdiflg


class MaximumLengthDifferenceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(mxdiflg([
            'hoqq', 'bbllkw', 'oox', 'ejjuyyy', 'plmiis', 'xxxzgpsssa',
            'xxwwkktt', 'znnnnfqknaz', 'qqquuhii', 'dvvvwz'
        ], ['cccooommaaqqoxii', 'gggqaffhhh', 'tttoowwwmmww']), 13)

    def test_equal_2(self):
        self.assertEqual(mxdiflg(['abc'], []), -1)
