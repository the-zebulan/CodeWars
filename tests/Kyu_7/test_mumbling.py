import unittest

from Kyu_7.mumbling import accum


class MumblingTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(accum('ZpglnRxqenU'),
                         'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqq'
                         'qq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu')

    def test_equals_2(self):
        self.assertEqual(accum('NyffsGeyylB'), 'N-Yy-Fff-Ffff-Sssss-Gggggg-E'
                                               'eeeeee-Yyyyyyyy-Yyyyyyyyy-Ll'
                                               'llllllll-Bbbbbbbbbbb')

    def test_equals_3(self):
        self.assertEqual(accum('MjtkuBovqrU'), 'M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-O'
                                               'oooooo-Vvvvvvvv-Qqqqqqqqq-Rr'
                                               'rrrrrrrr-Uuuuuuuuuuu')

    def test_equals_4(self):
        self.assertEqual(accum('EvidjUnokmM'), 'E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-N'
                                               'nnnnnn-Oooooooo-Kkkkkkkkk-Mm'
                                               'mmmmmmmm-Mmmmmmmmmmm')

    def test_equals_5(self):
        self.assertEqual(accum('HbideVbxncC'), 'H-Bb-Iii-Dddd-Eeeee-Vvvvvv-B'
                                               'bbbbbb-Xxxxxxxx-Nnnnnnnnn-Cc'
                                               'cccccccc-Ccccccccccc')


if __name__ == '__main__':
    unittest.main()
