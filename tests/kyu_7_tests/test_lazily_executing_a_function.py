import unittest
from operator import add, sub, mul, div, mod

from katas.kyu_7.lazily_executing_a_function import make_lazy


class MakeLazyTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(make_lazy(mod, 96, 38)(), mod(96, 38))

    def test_equal_2(self):
        self.assertEqual(make_lazy(mod, 73, 66)(), mod(73, 66))

    def test_equal_3(self):
        self.assertEqual(make_lazy(sub, 77, 73)(), sub(77, 73))

    def test_equal_4(self):
        self.assertEqual(make_lazy(mul, 12, 50)(), mul(12, 50))

    def test_equal_5(self):
        self.assertEqual(make_lazy(mod, 71, 64)(), mod(71, 64))

    def test_equal_6(self):
        self.assertEqual(make_lazy(mul, 62, 100)(), mul(62, 100))

    def test_equal_7(self):
        self.assertEqual(make_lazy(mod, 71, 99)(), mod(71, 99))

    def test_equal_8(self):
        self.assertEqual(make_lazy(sub, 11, 13)(), sub(11, 13))

    def test_equal_9(self):
        self.assertEqual(make_lazy(sub, 14, 82)(), sub(14, 82))

    def test_equal_10(self):
        self.assertEqual(make_lazy(mul, 91, 31)(), mul(91, 31))

    def test_equal_11(self):
        self.assertEqual(make_lazy(mod, 28, 37)(), mod(28, 37))

    def test_equal_12(self):
        self.assertEqual(make_lazy(add, 99, 43)(), add(99, 43))

    def test_equal_13(self):
        self.assertEqual(make_lazy(add, 43, 6)(), add(43, 6))

    def test_equal_14(self):
        self.assertEqual(make_lazy(mul, 78, 15)(), mul(78, 15))

    def test_equal_15(self):
        self.assertEqual(make_lazy(add, 66, 65)(), add(66, 65))

    def test_equal_16(self):
        self.assertEqual(make_lazy(mod, 79, 40)(), mod(79, 40))

    def test_equal_17(self):
        self.assertEqual(make_lazy(mod, 55, 73)(), mod(55, 73))

    def test_equal_18(self):
        self.assertEqual(make_lazy(mod, 99, 49)(), mod(99, 49))

    def test_equal_19(self):
        self.assertEqual(make_lazy(sub, 57, 19)(), sub(57, 19))

    def test_equal_20(self):
        self.assertEqual(make_lazy(sub, 17, 44)(), sub(17, 44))

    def test_equal_21(self):
        self.assertEqual(make_lazy(mod, 59, 40)(), mod(59, 40))

    def test_equal_22(self):
        self.assertEqual(make_lazy(add, 93, 90)(), add(93, 90))

    def test_equal_23(self):
        self.assertEqual(make_lazy(mul, 63, 78)(), mul(63, 78))

    def test_equal_24(self):
        self.assertEqual(make_lazy(div, 53, 41)(), div(53, 41))

    def test_equal_25(self):
        self.assertEqual(make_lazy(mul, 7, 17)(), mul(7, 17))

    def test_equal_26(self):
        self.assertEqual(make_lazy(div, 79, 68)(), div(79, 68))

    def test_equal_27(self):
        self.assertEqual(make_lazy(sub, 59, 76)(), sub(59, 76))

    def test_equal_28(self):
        self.assertEqual(make_lazy(add, 11, 67)(), add(11, 67))

    def test_equal_29(self):
        self.assertEqual(make_lazy(div, 91, 42)(), div(91, 42))

    def test_equal_30(self):
        self.assertEqual(make_lazy(mod, 8, 84)(), mod(8, 84))

    def test_equal_31(self):
        self.assertEqual(make_lazy(mod, 26, 14)(), mod(26, 14))

    def test_equal_32(self):
        self.assertEqual(make_lazy(mod, 59, 83)(), mod(59, 83))

    def test_equal_33(self):
        self.assertEqual(make_lazy(mul, 2, 84)(), mul(2, 84))

    def test_equal_34(self):
        self.assertEqual(make_lazy(mul, 78, 59)(), mul(78, 59))

    def test_equal_35(self):
        self.assertEqual(make_lazy(mul, 34, 78)(), mul(34, 78))

    def test_equal_36(self):
        self.assertEqual(make_lazy(div, 32, 100)(), div(32, 100))

    def test_equal_37(self):
        self.assertEqual(make_lazy(sub, 75, 1)(), sub(75, 1))

    def test_equal_38(self):
        self.assertEqual(make_lazy(mod, 37, 11)(), mod(37, 11))

    def test_equal_39(self):
        self.assertEqual(make_lazy(add, 29, 91)(), add(29, 91))

    def test_equal_40(self):
        self.assertEqual(make_lazy(add, 37, 29)(), add(37, 29))

    def test_equal_41(self):
        self.assertEqual(make_lazy(div, 14, 71)(), div(14, 71))

    def test_equal_42(self):
        self.assertEqual(make_lazy(add, 70, 56)(), add(70, 56))

    def test_equal_43(self):
        self.assertEqual(make_lazy(div, 69, 57)(), div(69, 57))

    def test_equal_44(self):
        self.assertEqual(make_lazy(sub, 87, 1)(), sub(87, 1))

    def test_equal_45(self):
        self.assertEqual(make_lazy(mod, 27, 94)(), mod(27, 94))

    def test_equal_46(self):
        self.assertEqual(make_lazy(mul, 18, 76)(), mul(18, 76))

    def test_equal_47(self):
        self.assertEqual(make_lazy(div, 5, 51)(), div(5, 51))

    def test_equal_48(self):
        self.assertEqual(make_lazy(mul, 63, 79)(), mul(63, 79))

    def test_equal_49(self):
        self.assertEqual(make_lazy(mul, 36, 48)(), mul(36, 48))

    def test_equal_50(self):
        self.assertEqual(make_lazy(mod, 14, 1)(), mod(14, 1))
