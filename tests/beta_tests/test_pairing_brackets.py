import unittest

from katas.beta.pairing_brackets import bracket_pairs


class BracketPairsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(bracket_pairs('len(list)'), {3: 8})

    def test_equal_2(self):
        self.assertEqual(bracket_pairs('Test Passed'), {})

    def test_equal_3(self):
        self.assertEqual(bracket_pairs('string'), {})

    def test_equal_4(self):
        self.assertEqual(bracket_pairs(''), {})

    def test_equal_5(self):
        self.assertEqual(bracket_pairs('(a(b)c()d)'), {0: 9, 2: 4, 6: 7})

    def test_equal_6(self):
        self.assertEqual(bracket_pairs('f(x[0])'), {1: 6})

    def test_equal_7(self):
        self.assertEqual(bracket_pairs('(()())(xxx)()()((()))'), {
            0: 5, 1: 2, 3: 4, 6: 10, 11: 12, 13: 14, 15: 20, 16: 19, 17: 18
        })

    def test_equal_8(self):
        self.assertEqual(bracket_pairs('()(x)(x)(x)(x((xx()))())xx()()'), {
            0: 1, 2: 4, 5: 7, 8: 10, 11: 23, 13: 20, 14: 19, 17: 18, 21: 22,
            26: 27, 28: 29
        })

    def test_equal_9(self):
        self.assertEqual(bracket_pairs('(x)x()((x))()(x)xx()()()x()'), {
            0: 2, 4: 5, 6: 10, 7: 9, 11: 12, 13: 15, 18: 19, 20: 21, 22: 23,
            25: 26
        })

    def test_equal_10(self):
        self.assertEqual(bracket_pairs('()(()xx)(x)()()()(x)'), {
            0: 1, 2: 7, 3: 4, 8: 10, 11: 12, 13: 14, 15: 16, 17: 19
        })

    def test_equal_11(self):
        self.assertEqual(bracket_pairs('((xxx)()()(xxxx()x))x(x)'), {
            0: 19, 1: 5, 6: 7, 8: 9, 10: 18, 15: 16, 21: 23
        })

    def test_equal_12(self):
        self.assertEqual(bracket_pairs('(x)x()(x)x(x)()()(x)((x))'), {
            0: 2, 4: 5, 6: 8, 10: 12, 13: 14, 15: 16, 17: 19, 20: 24, 21: 23
        })

    def test_equal_13(self):
        self.assertEqual(bracket_pairs('xx()(()())()()(())'), {
            2: 3, 4: 9, 5: 6, 7: 8, 10: 11, 12: 13, 14: 17, 15: 16
        })

    def test_equal_14(self):
        self.assertEqual(bracket_pairs('x(x)xxx((xxx(x((xx)(())x))))'), {
            1: 3, 7: 27, 8: 26, 12: 25, 14: 24, 15: 18, 19: 22, 20: 21
        })

    def test_equal_15(self):
        self.assertEqual(bracket_pairs('()()x()x(x)()(x(xx((x)x(()x)x)))'), {
            0: 1, 2: 3, 5: 6, 8: 10, 11: 12, 13: 31, 15: 30, 18: 29, 19: 21,
            23: 27, 24: 25
        })

    def test_equal_16(self):
        self.assertEqual(bracket_pairs('(xx)x()xx(x())()((())x)(xx)()()'), {
            0: 3, 5: 6, 9: 13, 11: 12, 14: 15, 16: 22, 17: 20, 18: 19, 23: 26,
            27: 28, 29: 30
        })

    def test_equal_17(self):
        self.assertEqual(bracket_pairs("(first)and(second)"), {0: 6, 10: 17})

    def test_false_1(self):
        self.assertFalse(bracket_pairs('def f(x'))

    def test_false_2(self):
        self.assertFalse(bracket_pairs(')('))

    def test_false_3(self):
        self.assertFalse(bracket_pairs('x)))x)xx)(x))x))(x)))))))))))x'))

    def test_false_4(self):
        self.assertFalse(bracket_pairs('xxxx)xx((('))

    def test_false_5(self):
        self.assertFalse(bracket_pairs('x))))))xx))(x'))

    def test_false_6(self):
        self.assertFalse(bracket_pairs(')(()((x)))x))))()(x))x'))

    def test_false_7(self):
        self.assertFalse(bracket_pairs('(x())(x))((x)(())))x())x)x))'))

    def test_false_8(self):
        self.assertFalse(bracket_pairs('()xx)()()())xx))(((x()())x())'))

    def test_false_9(self):
        self.assertFalse(bracket_pairs('xx()()))()xx()x)))))('))

    def test_false_10(self):
        self.assertFalse(bracket_pairs('x)))()((xxx()xx((xx(x('))

    def test_false_11(self):
        self.assertFalse(bracket_pairs(')x(x))x))()x))x((xx))x)x))'))

    def test_false_12(self):
        self.assertFalse(bracket_pairs('x)xx)'))

    def test_false_13(self):
        self.assertFalse(bracket_pairs("(first)and(second))"))

    def test_false_14(self):
        self.assertFalse(bracket_pairs("((first)and(second)"))


if __name__ == '__main__':
    unittest.main()
