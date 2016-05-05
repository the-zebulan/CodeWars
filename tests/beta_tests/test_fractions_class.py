import unittest

from katas.beta.fractions_class import Fraction


class FractionTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(Fraction(1, 8) + Fraction(4, 5), Fraction(37, 40))

    def test_equal_2(self):
        self.assertEqual(Fraction(911, 920) + Fraction(980, 906),
                         Fraction(863483, 416760))

    def test_equal_3(self):
        self.assertEqual(Fraction(610, 941) + Fraction(253, 985),
                         Fraction(838923, 926885))

    def test_equal_4(self):
        self.assertEqual(Fraction(956, 798) + Fraction(662, 189),
                         Fraction(16880, 3591))

    def test_equal_5(self):
        self.assertEqual(Fraction(694, 485) + Fraction(853, 861),
                         Fraction(1011239, 417585))

    def test_equal_6(self):
        self.assertEqual(Fraction(982, 111) + Fraction(219, 561),
                         Fraction(191737, 20757))

    def test_equal_7(self):
        self.assertEqual(Fraction(344, 873) + Fraction(658, 486),
                         Fraction(41201, 23571))

    def test_equal_8(self):
        self.assertEqual(Fraction(662, 361) + Fraction(322, 382),
                         Fraction(184563, 68951))

    def test_equal_9(self):
        self.assertEqual(Fraction(740, 813) + Fraction(184, 348),
                         Fraction(33926, 23577))

    def test_equal_10(self):
        self.assertEqual(Fraction(579, 441) + Fraction(543, 807),
                         Fraction(78524, 39543))

    def test_equal_11(self):
        self.assertEqual(Fraction(212, 979) + Fraction(46, 580),
                         Fraction(83997, 283910))


if __name__ == '__main__':
    unittest.main()
