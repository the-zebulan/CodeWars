import unittest

from katas.kyu_6.interlace_an_arbitrary_number_of_strings import \
    combine_strings


class CombineStringsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(combine_strings(), '')

    def test_equal_2(self):
        self.assertEqual(combine_strings('abc'), 'abc')

    def test_equal_3(self):
        self.assertEqual(combine_strings('abc', '123'), 'a1b2c3')

    def test_equal_4(self):
        self.assertEqual(combine_strings('abcd', '123'), 'a1b2c3d')

    def test_equal_5(self):
        self.assertEqual(combine_strings('abc', '1234'), 'a1b2c34')

    def test_equal_6(self):
        self.assertEqual(combine_strings('abc', '123', '$%'), 'a1$b2%c3')

    def test_equal_7(self):
        self.assertEqual(combine_strings('abcd', '123', '$%'), 'a1$b2%c3d')

    def test_equal_8(self):
        self.assertEqual(combine_strings('abcd', '123', '$%^&'), 'a1$b2%c3^d&')

    def test_equal_9(self):
        self.assertEqual(
            combine_strings('abcd', '123', '$%^&', 'qwertyuiop'),
            'a1$qb2%wc3^ed&rtyuiop')

    def test_equal_10(self):
        self.assertEqual(
            combine_strings('abcd', '123', '$%^&', 'qwertyuiop', 'X'),
            'a1$qXb2%wc3^ed&rtyuiop')
