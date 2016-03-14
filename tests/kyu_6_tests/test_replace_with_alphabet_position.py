import unittest

from kyu_6.replace_wth_alphabet_position import alphabet_position


class AlphabetPositionTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(alphabet_position(
            'The sunset sets at twelve o\' clock.'),
            '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12'
            ' 15 3 11')

    def test_equals_2(self):
        self.assertEqual(alphabet_position('The narwhal bacons at midnight.'),
                         '20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 '
                         '4 14 9 7 8 20')


if __name__ == '__main__':
    unittest.main()
