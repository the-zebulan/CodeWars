import unittest

from katas.beta.colored_hexes import hex_color


class HexColorTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(hex_color('000 000 000'), 'black')

    def test_equal_2(self):
        self.assertEqual(hex_color('121 245 255'), 'blue')

    def test_equal_3(self):
        self.assertEqual(hex_color('027 100 100'), 'cyan')

    def test_equal_4(self):
        self.assertEqual(hex_color('021 021 021'), 'white')

    def test_equal_5(self):
        self.assertEqual(hex_color('255 000 000'), 'red')

    def test_equal_6(self):
        self.assertEqual(hex_color('000 147 000'), 'green')

    def test_equal_7(self):
        self.assertEqual(hex_color('212 103 212'), 'magenta')

    def test_equal_8(self):
        self.assertEqual(hex_color('101 101 092'), 'yellow')

    def test_equal_9(self):
        self.assertEqual(hex_color(''), 'black')
