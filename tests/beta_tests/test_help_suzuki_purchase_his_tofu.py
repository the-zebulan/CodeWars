import unittest

from katas.beta.help_suzuki_purchase_his_tofu import buy_tofu


class BuyTofuTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(buy_tofu(
            124, 'mon mon mon mon mon apple mon mon mon mon mon mon mon mon'
                 'me mon mon monme mon mon mon mon cloth monme mon mon mon '
                 'mon mon mon mon mon cloth mon mon monme mon mon mon mon m'
                 'onme mon mon mon mon mon mon mon mon mon mon mon mon mon'
        ), [45, 5, 345, 6])

    def test_equal_2(self):
        self.assertEqual(buy_tofu(674, 'mon mon mon'), 'leaving the market')

    def test_equal_3(self):
        self.assertEqual(buy_tofu(1, 'monme mon mon monme'), [2, 2, 122, 1])

    def test_equal_4(self):
        self.assertEqual(buy_tofu(122, 'monme mon mon monme'), [2, 2, 122, 4])

    def test_equal_5(self):
        self.assertEqual(buy_tofu(
            124, 'mon mon mon mon mon apple mon mon mon mon mon mon mon mon'
                 ' mon mon mon mon mon mon mon mon mon mon mon mon mon mon '
                 'mon mon mon mon mon mon mon mon mon mon mon mon mon mon m'
                 'on mon mon mon mon mon mon mon mon mon mon mon mon mon mo'
                 'n mon mon mon mon mon mon mon mon mon mon mon mon mon mon'
                 ' mon mon mon mon mon mon mon mon mon mon mon mon mon mon '
                 'mon mon mon monme mon mon mon mon cloth mon mon mon mon m'
                 'on mon mon mon mon cloth mon mon mon mon mon mon mon mon '
                 'mon mon mon mon mon mon mon mon mon mon mon mon mon'
        ), [121, 1, 181, 65])
