import unittest

from katas.beta.esrever_esrever import esrever


class EsreverTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(esrever('an Easy one?'), 'eno ysaE na?')

    def test_equal_2(self):
        self.assertEqual(esrever('a small lOan OF 1,000,000 $!'),
                         '$ 000,000,1 FO naOl llams a!')

    def test_equal_3(self):
        self.assertEqual(esrever('<?> &!.".'), '".!& >?<.')

    def test_equal_4(self):
        self.assertEqual(esrever('b3tTer p4ss thIS 0ne.'),
                         'en0 SIht ss4p reTt3b.')

    def test_equal_5(self):
        self.assertEqual(esrever(''), '')
