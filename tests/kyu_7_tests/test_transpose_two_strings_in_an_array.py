import unittest

from katas.kyu_7.transpose_two_strings_in_an_array import transpose_two_strings


class TransposeTwoStringsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(transpose_two_strings(['Hello', 'World']),
                         'H W\ne o\nl r\nl l\no d')

    def test_equal_2(self):
        self.assertEqual(transpose_two_strings(['joey', 'louise']),
                         'j l\no o\ne u\ny i\n  s\n  e')

    def test_equal_3(self):
        self.assertEqual(transpose_two_strings(['a', 'cat']), 'a c\n  a\n  t')

    def test_equal_4(self):
        self.assertEqual(transpose_two_strings(['cat', '']), 'c  \na  \nt  ')

    def test_equal_5(self):
        self.assertEqual(transpose_two_strings(['!a!a!', '?b?b']),
                         '! ?\na b\n! ?\na b\n!  ')
