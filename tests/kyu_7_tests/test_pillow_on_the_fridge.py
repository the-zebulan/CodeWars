import unittest

from katas.kyu_7.pillow_on_the_fridge import pillow


class PillowTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(pillow(['n', 'B']))

    def test_true_2(self):
        self.assertTrue(pillow(['yF[CeAAiNihWEmKxJc/NRMVn',
                                'rMeIa\\KAfbjuLiTnAQxNw[XB']))

    def test_true_3(self):
        self.assertTrue(pillow(['inECnBMAA/u', 'ABAaIUOUx/M']))

    def test_false_1(self):
        self.assertFalse(pillow(['EvH/KNikBiyxfeyK/miCMj',
                                 'I/HwjnHlFLlahMOKNadps']))

    def test_false_2(self):
        self.assertFalse(pillow(['\\DjQ\\[zv]SpG]Z/[Qm\\eLL',
                                 'amwZArsaGRmibriXBgTRZp']))
