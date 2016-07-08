import unittest

from katas.beta.print_that_calendar import show_calendar


class ShowCalendarTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(
            show_calendar(2001, 10),
            '    October 2001\n'
            'Mo Tu We Th Fr Sa Su\n'
            ' 1  2  3  4  5  6  7\n'
            ' 8  9 10 11 12 13 14\n'
            '15 16 17 18 19 20 21\n'
            '22 23 24 25 26 27 28\n'
            '29 30 31\n'
        )

    def test_equal_2(self):
        self.assertEqual(
            show_calendar(2016, 5),
            '      May 2016\n'
            'Mo Tu We Th Fr Sa Su\n'
            '                   1\n'
            ' 2  3  4  5  6  7  8\n'
            ' 9 10 11 12 13 14 15\n'
            '16 17 18 19 20 21 22\n'
            '23 24 25 26 27 28 29\n'
            '30 31\n'
        )

    def test_equal_3(self):
        self.assertEqual(
            show_calendar(2015, 12),
            '   December 2015\n'
            'Mo Tu We Th Fr Sa Su\n'
            '    1  2  3  4  5  6\n'
            ' 7  8  9 10 11 12 13\n'
            '14 15 16 17 18 19 20\n'
            '21 22 23 24 25 26 27\n'
            '28 29 30 31\n'
        )


if __name__ == '__main__':
    unittest.main()
