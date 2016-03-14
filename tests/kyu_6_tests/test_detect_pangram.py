import unittest

from kyu_6.detect_pangram import is_pangram


class DetectPangramTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_pangram(
            'The quick, brown fox jumps over the lazy dog!'))

    def test_true_2(self):
        self.assertTrue(is_pangram('Cwm fjord bank glyphs vext quiz'))

    def test_true_3(self):
        self.assertTrue(is_pangram(
            'Pack my box with five dozen liquor jugs.'))

    def test_true_4(self):
        self.assertTrue(is_pangram('How quickly daft jumping zebras vex.'))

    def test_true_5(self):
        self.assertTrue(is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'))

    def test_false(self):
        self.assertFalse(is_pangram('This isn\'t a pangram!'))

    def test_false_2(self):
        self.assertFalse(is_pangram('abcdefghijklmopqrstuvwxyz'))


if __name__ == '__main__':
    unittest.main()
