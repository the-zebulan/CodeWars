import unittest

from katas.kyu_7.suzuki_needs_help_lining_up_his_students import \
    lineup_students


class LineupStudentsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(lineup_students(
            'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi '
            'Takeshi'), ['Takehiko', 'Takayuki', 'Takahiro', 'Takeshi',
                         'Takeshi', 'Takashi', 'Tadashi', 'Takeo', 'Takao'])

    def test_equals_2(self):
        self.assertEqual(lineup_students(
            'Michio Miki Mikio Minori Minoru Mitsuo Mitsuru Nao Naoki Naoko '
            'Noboru Nobu Nobuo ,Nobuyuki Nori Norio Osamu Rafu Raiden Ringo '
            'Rokuro Ronin Ryo Ryoichi Ryota Ryozo Ryuichi Ryuu Saburo Sadao '
            'Samuru Satoru Satoshi Seiichi Seiji Senichi Shichiro Shig Shige'
            'kazu Shigeo Shigeru Shima Shin Shinichi Shinji Shiro Shoichi Sh'
            'oji Shuichi Shuji Shunichi Susumu Tadao Tadashi Takahiro Takao '
            'Takashi Takayuki Takehiko Takeo Takeshi Takeshi Takumi Tama Tam'
            'otsu Taro Tatsuo Tatsuya Teruo Tetsip Tetsuya Tomi Tomio Toru T'
            'oshi Toshiaki Toshihiro Toshio Toshiyuki Toyo Tsuneo Tsutomu Ts'
            'uyoshi Uyeda Yasahiro Yasuhiro Yasuo Yasushi Yemon Yogi Yoichi '
            'Yori Yoshi Yoshiaki Yoshihiro Yoshikazu Yoshimitsu Yoshinori Yo'
            'shio Yoshiro Yoshito Yoshiyuki Yuichi Yuji Yuki'),
            ['Yoshimitsu', 'Yoshiyuki', 'Yoshinori', 'Yoshikazu',
             'Yoshihiro', 'Toshiyuki', 'Toshihiro', 'Shigekazu', ',Nobuyuki',
             'Yoshiaki', 'Yasuhiro', 'Yasahiro', 'Tsuyoshi', 'Toshiaki',
             'Takehiko', 'Takayuki', 'Takahiro', 'Shunichi', 'Shinichi',
             'Shichiro', 'Yoshito', 'Yoshiro', 'Yasushi', 'Tsutomu',
             'Tetsuya', 'Tatsuya', 'Tamotsu', 'Takeshi', 'Takeshi',
             'Takashi', 'Tadashi', 'Shuichi', 'Shoichi', 'Shigeru',
             'Senichi', 'Seiichi', 'Satoshi', 'Ryuichi', 'Ryoichi',
             'Mitsuru', 'Yuichi', 'Yoshio', 'Yoichi', 'Tsuneo', 'Toshio',
             'Tetsip', 'Tatsuo', 'Takumi', 'Susumu', 'Shinji', 'Shigeo',
             'Satoru', 'Samuru', 'Saburo', 'Rokuro', 'Raiden', 'Noboru',
             'Mitsuo', 'Minoru', 'Minori', 'Michio', 'Yoshi', 'Yemon',
             'Yasuo', 'Uyeda', 'Toshi', 'Tomio', 'Teruo', 'Takeo', 'Takao',
             'Tadao', 'Shuji', 'Shoji', 'Shiro', 'Shima', 'Seiji', 'Sadao',
             'Ryozo', 'Ryota', 'Ronin', 'Ringo', 'Osamu', 'Norio', 'Nobuo',
             'Naoko', 'Naoki', 'Mikio', 'Yuki', 'Yuji', 'Yori', 'Yogi',
             'Toyo', 'Toru', 'Tomi', 'Taro', 'Tama', 'Shin', 'Shig',
             'Ryuu', 'Rafu', 'Nori', 'Nobu', 'Miki', 'Ryo', 'Nao'])
