import unittest

from katas.kyu_7.scaling_squared_strings import scale


class ScaleTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(scale("", 5, 5), "")

    def test_equal_2(self):
        self.assertEqual(scale("Kj\nSH", 1, 2), "Kj\nKj\nSH\nSH")

    def test_equal_3(self):
        self.assertEqual(scale("abcd\nefgh\nijkl\nmnop", 2, 3), "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp")

    def test_equal_4(self):
        self.assertEqual(scale("lxnT\nqiut\nZZll\nFElq", 1, 2), "lxnT\nlxnT\nqiut\nqiut\nZZll\nZZll\nFElq\nFElq")

    def test_equal_5(self):
        self.assertEqual(scale("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 2, 2), "YYVVjjoossWW\nYYVVjjoossWW\nHHGGhhKKGGZZ\nHHGGhhKKGGZZ\nLLHHNNMMLLmm\nLLHHNNMMLLmm\nJJttccWWCCjj\nJJttccWWCCjj\nggVVttjjyykk\nggVVttjjyykk\nOOJJBBkkOOKK\nOOJJBBkkOOKK")

    def test_equal_6(self):
        self.assertEqual(scale("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 1, 2), "YVjosW\nYVjosW\nHGhKGZ\nHGhKGZ\nLHNMLm\nLHNMLm\nJtcWCj\nJtcWCj\ngVtjyk\ngVtjyk\nOJBkOK\nOJBkOK")

    def test_equal_7(self):
        self.assertEqual(scale("WgaB\nMmIn\nqJwv\nAhho", 2, 1), "WWggaaBB\nMMmmIInn\nqqJJwwvv\nAAhhhhoo")

    def test_equal_8(self):
        self.assertEqual(scale("CG\nla", 2, 3), "CCGG\nCCGG\nCCGG\nllaa\nllaa\nllaa")


if __name__ == '__main__':
    unittest.main()
