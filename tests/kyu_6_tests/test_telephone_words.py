import unittest

from katas.kyu_6.telephone_words import telephoneWords


class TelephoneWordsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(telephoneWords('0002'), {'000A', '000B', '000C'})

    def test_equal_2(self):
        self.assertEqual(telephoneWords('1123'), {
            '11AD', '11AE', '11AF', '11BD', '11BE', '11BF', '11CD', '11CE',
            '11CF'})

    def test_equal_3(self):
        self.assertEqual(telephoneWords('1234'), {
            '1ADG', '1ADH', '1ADI', '1AEG', '1AEH', '1AEI', '1AFG', '1AFH',
            '1AFI', '1BDG', '1BDH', '1BDI', '1BEG', '1BEH', '1BEI', '1BFG',
            '1BFH', '1BFI', '1CDG', '1CDH', '1CDI', '1CEG', '1CEH', '1CEI',
            '1CFG', '1CFH', '1CFI'})

    def test_equal_4(self):
        self.assertEqual(telephoneWords('5987'), {
            'JXVP', 'JXVQ', 'JXVR', 'JXVS', 'JZUS', 'JZUR', 'JZUQ', 'JZUP',
            'LYUR', 'LYUS', 'KXUR', 'KXUS', 'KXUP', 'KXUQ', 'LYUQ', 'LWVQ',
            'LWVP', 'LWVS', 'LWVR', 'KWVP', 'KWVQ', 'KWVR', 'KWVS', 'LXVR',
            'JZTP', 'JZTQ', 'JZTR', 'JZTS', 'KXVS', 'KXVR', 'KXVQ', 'KXVP',
            'KYVR', 'KYVS', 'KYVP', 'KYVQ', 'JXTR', 'JXTS', 'JXTP', 'JXTQ',
            'JYTS', 'JYTR', 'JYTQ', 'JYTP', 'LZTR', 'LZTS', 'KWUQ', 'KWUP',
            'KWUS', 'KWUR', 'LZTP', 'LZTQ', 'JYUP', 'JYUQ', 'JYUR', 'JYUS',
            'JZVR', 'JZVS', 'JZVP', 'JZVQ', 'KXTQ', 'KXTP', 'KXTS', 'KXTR',
            'KWTR', 'KWTS', 'KWTP', 'KWTQ', 'LZUS', 'LZUQ', 'LZUP', 'JYVQ',
            'JYVP', 'JYVS', 'JYVR', 'LZUR', 'JWVS', 'JWVR', 'JWVQ', 'JWVP',
            'LXUS', 'LXUR', 'LXUQ', 'LXUP', 'KZTS', 'KZTR', 'KZTQ', 'KZTP',
            'JXUQ', 'JXUP', 'JXUS', 'JXUR', 'LYVS', 'LXTP', 'LXTQ', 'LXTR',
            'LXTS', 'KZUP', 'KZUQ', 'KZUR', 'KZUS', 'LYTQ', 'LYTP', 'LYTS',
            'LYTR', 'LXVQ', 'LZVP', 'LZVQ', 'LZVR', 'LZVS', 'LYUP', 'KYUS',
            'KYUR', 'KYUQ', 'KYUP', 'LXVS', 'LXVP', 'LWTS', 'LWTR', 'LWTQ',
            'LWTP', 'JWTQ', 'JWTP', 'JWTS', 'JWTR', 'LYVR', 'KZVQ', 'LYVQ',
            'KZVP', 'LYVP', 'KZVS', 'KZVR', 'KYTP', 'KYTQ', 'KYTR', 'KYTS',
            'LWUP', 'LWUQ', 'LWUR', 'LWUS', 'JWUR', 'JWUS', 'JWUP', 'JWUQ'})
