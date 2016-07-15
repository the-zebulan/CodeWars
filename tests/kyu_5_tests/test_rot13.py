import unittest

from katas.kyu_5.rot13 import rot13


class ROT13TestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(rot13('EBG13 rknzcyr.'), 'ROT13 example.')

    def test_equals_2(self):
        self.assertEqual(rot13('This is my first ROT13 excercise!'),
                         'Guvf vf zl svefg EBG13 rkprepvfr!')

    def test_equals_3(self):
        self.assertEqual(rot13('Va gur ryringbef, gur rkgebireg ybbxf ng gur'
                               ' BGURE thl\'f fubrf.'),
                         'In the elevators, the extrovert looks at the OTHER'
                         ' guy\'s shoes.')
