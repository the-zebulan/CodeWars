import unittest

from katas.kyu_5.second_variation_on_caesar_cipher import encode_str, decode


class CaesarCipherTestCase(unittest.TestCase):
    def setUp(self):
        self.s1 = \
            'I should have known that you would have a perfect answer for me!!!'
        self.s2 = 'O CAPTAIN! my Captain! our fearful trip is done;'
        self.lst1 = ['ijJ tipvme ibw', 'f lopxo uibu z', 'pv xpvme ibwf ',
                     'b qfsgfdu botx', 'fs gps nf!!!']
        self.lst2 = ['opP DBQUBJ', 'O! nz Dbqu', 'bjo! pvs g',
                     'fbsgvm usj', 'q jt epof;']

    def test_equals(self):
        self.assertEqual(decode(self.lst1), self.s1)

    def test_equals_2(self):
        self.assertEqual(encode_str(self.s1, 1), self.lst1)

    def test_equals_3(self):
        self.assertEqual(decode(self.lst2), self.s2)

    def test_equals_4(self):
        self.assertEqual(encode_str(self.s2, 1), self.lst2)


if __name__ == '__main__':
    unittest.main()
