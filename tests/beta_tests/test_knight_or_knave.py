import unittest

from katas.beta.knight_or_knave import knight_or_knave


class KnightOrKnaveTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(knight_or_knave(True), 'Knight!')

    def test_equal_2(self):
        self.assertEqual(knight_or_knave(False), 'Knave! Do not trust.')

    def test_equal_3(self):
        self.assertEqual(knight_or_knave('4+2==5'), 'Knave! Do not trust.')

    def test_equal_4(self):
        self.assertEqual(knight_or_knave('2+2==4'), 'Knight!')

    def test_equal_5(self):
        self.assertEqual(knight_or_knave(True and False),
                         'Knave! Do not trust.')

    def test_equal_6(self):
        self.assertEqual(knight_or_knave(True or False), 'Knight!')

    def test_equal_7(self):
        self.assertEqual(knight_or_knave(not False), 'Knight!')

    def test_equal_8(self):
        self.assertEqual(knight_or_knave(
            'not True and False or False or False'
        ), 'Knave! Do not trust.')

    def test_equal_9(self):
        self.assertEqual(knight_or_knave('3 is 3'), 'Knight!')

    def test_equal_10(self):
        self.assertEqual(knight_or_knave(not False), 'Knight!')

    def test_equal_11(self):
        self.assertEqual(knight_or_knave('True'), 'Knight!')

    def test_equal_12(self):
        self.assertEqual(knight_or_knave('not True'), 'Knave! Do not trust.')

    def test_equal_13(self):
        self.assertEqual(knight_or_knave('True'), 'Knight!')

    def test_equal_14(self):
        self.assertEqual(knight_or_knave(False), 'Knave! Do not trust.')

    def test_equal_15(self):
        self.assertEqual(knight_or_knave('2+2==5'), 'Knave! Do not trust.')

    def test_equal_16(self):
        self.assertEqual(knight_or_knave('4+1==5'), 'Knight!')

    def test_equal_17(self):
        self.assertEqual(knight_or_knave(True and False),
                         'Knave! Do not trust.')

    def test_equal_18(self):
        self.assertEqual(knight_or_knave(True or False), 'Knight!')

    def test_equal_19(self):
        self.assertEqual(knight_or_knave(not False), 'Knight!')

    def test_equal_20(self):
        self.assertEqual(knight_or_knave(
            not False and True or False or True
        ), 'Knight!')

    def test_equal_21(self):
        self.assertEqual(knight_or_knave('4 is 3'), 'Knave! Do not trust.')

    def test_equal_22(self):
        self.assertEqual(knight_or_knave(not False), 'Knight!')

    def test_equal_23(self):
        self.assertEqual(knight_or_knave('True'), 'Knight!')

    def test_equal_24(self):
        self.assertEqual(knight_or_knave('not True'), 'Knave! Do not trust.')

    def test_equal_25(self):
        self.assertEqual(knight_or_knave(False or False or False and False),
                         'Knave! Do not trust.')

    def test_equal_26(self):
        self.assertEqual(knight_or_knave(False), 'Knave! Do not trust.')

    def test_equal_27(self):
        self.assertEqual(knight_or_knave('9+2==3'), 'Knave! Do not trust.')

    def test_equal_28(self):
        self.assertEqual(knight_or_knave('105+30076==30181'), 'Knight!')

    def test_equal_29(self):
        self.assertEqual(knight_or_knave(True and False),
                         'Knave! Do not trust.')

    def test_equal_30(self):
        self.assertEqual(knight_or_knave(True or False), 'Knight!')

    def test_equal_31(self):
        self.assertEqual(knight_or_knave(not False), 'Knight!')

    def test_equal_32(self):
        self.assertEqual(knight_or_knave(
            'not True and False or False or False'
        ), 'Knave! Do not trust.')

    def test_equal_33(self):
        self.assertEqual(knight_or_knave('3 is 3 is 3 is 9'),
                         'Knave! Do not trust.')

    def test_equal_34(self):
        self.assertEqual(knight_or_knave(not False), 'Knight!')

    def test_equal_35(self):
        self.assertEqual(knight_or_knave('True'), 'Knight!')

    def test_equal_36(self):
        self.assertEqual(knight_or_knave('not True'), 'Knave! Do not trust.')

    def test_equal_37(self):
        self.assertEqual(knight_or_knave('True'), 'Knight!')

    def test_equal_38(self):
        self.assertEqual(knight_or_knave('False'), 'Knave! Do not trust.')

    def test_equal_39(self):
        self.assertEqual(knight_or_knave('2+2==5'), 'Knave! Do not trust.')

    def test_equal_40(self):
        self.assertEqual(knight_or_knave('4+1==5'), 'Knight!')

    def test_equal_41(self):
        self.assertEqual(knight_or_knave(True and False),
                         'Knave! Do not trust.')

    def test_equal_42(self):
        self.assertEqual(knight_or_knave(not False and not False), 'Knight!')

    def test_equal_43(self):
        self.assertEqual(knight_or_knave('"orange" is not "red"'), 'Knight!')

    def test_equal_44(self):
        self.assertEqual(knight_or_knave(
            not False and True or False or True
        ), 'Knight!')

    def test_equal_45(self):
        self.assertEqual(knight_or_knave('4 is "blue"'),
                         'Knave! Do not trust.')

    def test_equal_46(self):
        self.assertEqual(knight_or_knave(not False), 'Knight!')

    def test_equal_47(self):
        self.assertEqual(knight_or_knave('True is not False'), 'Knight!')

    def test_equal_48(self):
        self.assertEqual(knight_or_knave('not True'), 'Knave! Do not trust.')


if __name__ == '__main__':
    unittest.main()
