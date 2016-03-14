import unittest

from Kyu_6.eighties_kids_4_legends_of_the_hidden_temple import mark_spot


class MarkSpotTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(mark_spot(1), 'X\n')

    def test_equals_2(self):
        self.assertEqual(mark_spot(5),
                         'X       X\n  X   X\n    X\n  X   X\nX       X\n')

    def test_equals_3(self):
        self.assertEqual(mark_spot(11),
                         'X                   X\n  X               X\n'
                         '    X           X\n      X       X\n        '
                         'X   X\n          X\n        X   X\n      X  '
                         '     X\n    X           X\n  X              '
                         ' X\nX                   X\n')

    def test_equals_4(self):
        self.assertEqual(mark_spot([]), '?')

    def test_equals_5(self):
        self.assertEqual(mark_spot('treasure'), '?')

    def test_equals_6(self):
        self.assertEqual(mark_spot(-1), '?')


if __name__ == '__main__':
    unittest.main()
