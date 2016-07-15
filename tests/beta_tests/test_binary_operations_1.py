import unittest

from katas.beta.binary_operations_1 import flip_bit


class FlipBitTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(flip_bit(127, 8), 255)

    def test_equal_2(self):
        self.assertEqual(flip_bit(0, 16), 32768)

    def test_equal_3(self):
        self.assertEqual(flip_bit(2147483647, 31), 1073741823)

    def test_equal_4(self):
        self.assertEqual(flip_bit(9223372036854775806, 1),
                         9223372036854775807)

    def test_equal_5(self):
        self.assertEqual(flip_bit(4269501597640414366, 44),
                         4269510393733436574)

    def test_equal_6(self):
        self.assertEqual(flip_bit(15126664580577030336, 38),
                         15126664718015983808)

    def test_equal_7(self):
        self.assertEqual(flip_bit(7419769990796082583, 25),
                         7419769990812859799)

    def test_equal_8(self):
        self.assertEqual(flip_bit(8961092347735479934, 38),
                         8961092485174433406)

    def test_equal_9(self):
        self.assertEqual(flip_bit(13954711414747360827, 29),
                         13954711414478925371)

    def test_equal_10(self):
        self.assertEqual(flip_bit(11340252406009775956, 35),
                         11340252423189645140)

    def test_equal_11(self):
        self.assertEqual(flip_bit(1982674869837396906, 25),
                         1982674869820619690)

    def test_equal_12(self):
        self.assertEqual(flip_bit(15660359706141292060, 12),
                         15660359706141294108)

    def test_equal_13(self):
        self.assertEqual(flip_bit(2748006704688635354, 36),
                         2748006670328896986)

    def test_equal_14(self):
        self.assertEqual(flip_bit(3345196192679608119, 52),
                         3342944392865922871)

    def test_equal_15(self):
        self.assertEqual(flip_bit(5255269221387608593, 27),
                         5255269221454717457)

    def test_equal_16(self):
        self.assertEqual(flip_bit(15045200874639924045, 4),
                         15045200874639924037)

    def test_equal_17(self):
        self.assertEqual(flip_bit(12114637009352198324, 49),
                         12114355534375487668)

    def test_equal_18(self):
        self.assertEqual(flip_bit(17243841376559575648, 38),
                         17243841513998529120)

    def test_equal_19(self):
        self.assertEqual(flip_bit(6462998462590420465, 8),
                         6462998462590420337)

    def test_equal_20(self):
        self.assertEqual(flip_bit(15470130116804208774, 37),
                         15470130185523685510)

    def test_equal_21(self):
        self.assertEqual(flip_bit(7852939915545965202, 26),
                         7852939915579519634)

    def test_equal_22(self):
        self.assertEqual(flip_bit(9270848595918946572, 63),
                         13882534614346334476)

    def test_equal_23(self):
        self.assertEqual(flip_bit(7562489152403392331, 4),
                         7562489152403392323)

    def test_equal_24(self):
        self.assertEqual(flip_bit(2189951082260115788, 52),
                         2192202882073801036)
