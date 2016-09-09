import unittest

from katas.beta.range_parser import range_parser


class RangeParserTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(range_parser('1-10,14, 20-25:2'),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24])

    def test_equal_2(self):
        self.assertEqual(range_parser('5-10'), [5, 6, 7, 8, 9, 10])

    def test_equal_3(self):
        self.assertEqual(range_parser('2'), [2])

    def test_equal_4(self):
        self.assertEqual(range_parser('1-10,3'),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3])

    def test_equal_5(self):
        self.assertEqual(range_parser('1-10'), range_parser('1-10:1'))

    def test_equal_6(self):
        self.assertEqual(range_parser('1-10:5'), [1, 6])
