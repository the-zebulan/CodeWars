import unittest

from katas.beta.how_much_hex_is_the_fish import fisHex


class FisHexTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(fisHex('redlionfish'), 12)

    def test_equal_2(self):
        self.assertEqual(fisHex('pufferfish'), 1)

    def test_equal_3(self):
        self.assertEqual(fisHex('puffers'), 14)

    def test_equal_4(self):
        self.assertEqual(fisHex('balloonfish'), 14)

    def test_equal_5(self):
        self.assertEqual(fisHex('blowfish'), 4)

    def test_equal_6(self):
        self.assertEqual(fisHex('bubblefish'), 10)

    def test_equal_7(self):
        self.assertEqual(fisHex('globefish'), 10)

    def test_equal_8(self):
        self.assertEqual(fisHex('swellfish'), 1)

    def test_equal_9(self):
        self.assertEqual(fisHex('toadfish'), 8)

    def test_equal_10(self):
        self.assertEqual(fisHex('toadies'), 9)

    def test_equal_11(self):
        self.assertEqual(fisHex('honey toads'), 9)

    def test_equal_12(self):
        self.assertEqual(fisHex('sugar toads'), 13)

    def test_equal_13(self):
        self.assertEqual(fisHex('sea squab'), 5)


if __name__ == '__main__':
    unittest.main()
