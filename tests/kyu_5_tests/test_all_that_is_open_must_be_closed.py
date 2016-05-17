import unittest

from katas.kyu_5.all_that_is_open_must_be_closed import is_balanced


class IsBalancedTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(is_balanced('(Sensei says yes!)', '()'))

    def test_true_2(self):
        self.assertTrue(is_balanced('(Sensei [says] yes!)', '()[]'))

    def test_true_3(self):
        self.assertTrue(is_balanced('Sensei says -yes-!', '--'))

    def test_true_4(self):
        self.assertTrue(is_balanced('Hello Mother can you hear me?', '()'))

    def test_true_5(self):
        self.assertTrue(is_balanced('(Hello Mother can you hear me?)', '()'))

    def test_true_6(self):
        self.assertTrue(is_balanced('(Hello Mother can you hear me?', ''))

    def test_true_7(self):
        self.assertTrue(is_balanced(
            '(Hello Mother can you hear me?)[Monkeys, in my pockets!!]',
            '()[]'
        ))

    def test_true_8(self):
        self.assertTrue(is_balanced(
            '(Hello Mother can you hear me?)[Monkeys, in my pockets!!](Gosh'
            '!!)', '()[]'
        ))

    def test_true_9(self):
        self.assertTrue(is_balanced('((Hello))', '()'))

    def test_true_10(self):
        self.assertTrue(is_balanced('(((Hello)))', '()'))

    def test_true_11(self):
        self.assertTrue(is_balanced('((()Hello()))', '()'))

    def test_true_12(self):
        self.assertTrue(is_balanced('([{-Hello!-}])', '()[]{}'))

    def test_true_13(self):
        self.assertTrue(is_balanced('([{([{Hello}])}])', '()[]{}'))

    def test_true_14(self):
        self.assertTrue(is_balanced('-abcd-e@fghi@', '--@@'))

    def test_true_15(self):
        self.assertTrue(is_balanced('-Hello Mother can you hear me?-', '--'))

    def test_true_16(self):
        self.assertTrue(is_balanced('-a@b@cd@e@fghi-', '--@@'))

    def test_false_1(self):
        self.assertFalse(is_balanced('(Sensei says no!', '()'))

    def test_false_2(self):
        self.assertFalse(is_balanced('(Sensei [says) no!]', '()[]'))

    def test_false_3(self):
        self.assertFalse(is_balanced('Sensei -says no!', '--'))

    def test_false_4(self):
        self.assertFalse(is_balanced('(Hello Mother can you hear me?', '()'))

    def test_false_5(self):
        self.assertFalse(is_balanced(
            '(Hello Mother can you hear me?))', '()'
        ))

    def test_false_6(self):
        self.assertFalse(is_balanced(')Hello Mother can you hear me?', '()'))

    def test_false_7(self):
        self.assertFalse(is_balanced(
            'Hello Mother can you hear me?)[Monkeys, in my pockets!!]',
            '()[]'
        ))

    def test_false_8(self):
        self.assertFalse(is_balanced(
            '(Hello Mother can you hear me?[Monkeys, in my pockets!!]',
            '()[]'
        ))

    def test_false_9(self):
        self.assertFalse(is_balanced(
            '(Hello Mother can you hear me?)Monkeys, in my pockets!!]',
            '()[]'
        ))

    def test_false_10(self):
        self.assertFalse(is_balanced(
            '(Hello Mother can you hear me?)[Monkeys, in my pockets!!',
            '()[]'
        ))

    def test_false_11(self):
        self.assertFalse(is_balanced('((()Hello())', '()'))

    def test_false_12(self):
        self.assertFalse(is_balanced('(()Hello()))', '()'))

    def test_false_13(self):
        self.assertFalse(is_balanced('([{-Hello!-})]', '()[]{}'))

    def test_false_14(self):
        self.assertFalse(is_balanced('-Hello Mother can you hear me?', '--'))

    def test_false_15(self):
        self.assertFalse(is_balanced('Hello Mother can you hear me?-', '--'))

    def test_false_16(self):
        self.assertFalse(is_balanced('abcd-e@fghi@', '--@@'))

    def test_false_17(self):
        self.assertFalse(is_balanced('-abcde@fghi@', '--@@'))

    def test_false_18(self):
        self.assertFalse(is_balanced('-abcd-efghi@', '--@@'))

    def test_false_19(self):
        self.assertFalse(is_balanced('-abcd-e@fghi', '--@@'))

    def test_false_20(self):
        self.assertFalse(is_balanced('-ab@cd@e@fghi-', '--@@'))

    def test_false_21(self):
        self.assertFalse(is_balanced('-a@bcd@e@fghi-', '--@@'))

    def test_false_22(self):
        self.assertFalse(is_balanced('-a@b@cde@fghi-', '--@@'))

    def test_false_23(self):
        self.assertFalse(is_balanced('-a@b@cd@efghi-', '--@@'))

    def test_false_24(self):
        self.assertFalse(is_balanced('a@b@cd@e@fghi-', '--@@'))

    def test_false_25(self):
        self.assertFalse(is_balanced('-a@b@cd@e@fghi', '--@@'))


if __name__ == '__main__':
    unittest.main()
