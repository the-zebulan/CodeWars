# coding=utf-8
import unittest

from katas.kyu_7.the_ladies_of_eniac import rad_ladies


class RadLadiesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(rad_ladies('k?%35a&&/y@@@£5599 m93753&$$$c$n///79u?'
                                    '?@@%l?975$t?%5y%&$3$1!'), 'KAY MCNULTY!')

    def test_equals_2(self):
        self.assertEqual(rad_ladies('9?9?9?m335%$£@a791%&$r$$$l£@53$&y&n%$5@'
                                    ' $£5577w&7e931%s$£c$o%%%f351f??%!%%'),
                         'MARLYN WESCOFF!')

    def test_equals_3(self):
        self.assertEqual(rad_ladies('%&$557f953//1/$£@%r%935$$£a@£3111$@???%'
                                    'n???5 $%157b%///$i%55&31£@l?%&$$a%@£$s5'
                                    '757!$$%%%%53'), 'FRAN BILAS!')

    def test_equals_4(self):
        self.assertEqual(rad_ladies('///$%&£$553791£r357%??@$%u?$%@7993111£@'
                                    '$%t£$h3% 3$£l$311i3%@?&c3£h%&t&&?%11e%$'
                                    '?@11957r79%£&£m$$a55n1!111%%'),
                         'RUTH LICHTERMAN!')

    def test_equals_5(self):
        self.assertEqual(rad_ladies('??£@%&a5d15??e599713%l%%e%75913 1£$%&@g'
                                    '@£%o&$@13l5d11s$%&t15i9n&5%%@%e@£$!£%$£'),
                         'ADELE GOLDSTINE!')
