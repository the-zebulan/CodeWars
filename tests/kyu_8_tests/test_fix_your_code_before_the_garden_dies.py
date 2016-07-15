import unittest

from katas.kyu_8.fix_your_code_before_the_garden_dies import rain_amount


class RainAmountTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(
            rain_amount(100),
            'Your plant has had more than enough water for today!'
        )

    def test_equal_2(self):
        self.assertEqual(
            rain_amount(40),
            'Your plant has had more than enough water for today!'
        )

    def test_equal_3(self):
        self.assertEqual(rain_amount(39),
                         'You need to give your plant 1mm of water')

    def test_equal_4(self):
        self.assertEqual(rain_amount(5),
                         'You need to give your plant 35mm of water')

    def test_equal_5(self):
        self.assertEqual(rain_amount(0),
                         'You need to give your plant 40mm of water')
