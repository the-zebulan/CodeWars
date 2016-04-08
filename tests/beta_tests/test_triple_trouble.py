import unittest

from katas.beta.triple_trouble import triple_trouble


class TripleTroubleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(triple_trouble('aaa', 'bbb', 'ccc'), 'abcabcabc')

    def test_equals_2(self):
        self.assertEqual(triple_trouble('aaaaaa', 'bbbbbb', 'cccccc'),
                         'abcabcabcabcabcabc')

    def test_equals_3(self):
        self.assertEqual(triple_trouble('burn', 'reds', 'rolls'),
                         'brrueordlnsl')

    def test_equals_4(self):
        self.assertEqual(triple_trouble('Bm', 'aa', 'tn'), 'Batman')

    def test_equals_5(self):
        self.assertEqual(triple_trouble('LLh', 'euo', 'xtr'), 'LexLuthor')


if __name__ == '__main__':
    unittest.main()
