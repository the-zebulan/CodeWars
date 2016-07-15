import unittest

from katas.kyu_3.did_you_mean import Dictionary


class DidYouMeanTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(Dictionary([
            'cherry', 'peach', 'pineapple', 'melon', 'strawberry',
            'raspberry', 'apple', 'coconut', 'banana'
        ]).find_most_similar('strawbery'), 'strawberry')

    def test_equal_2(self):
        self.assertEqual(Dictionary([
            'cherry', 'peach', 'pineapple', 'melon', 'strawberry',
            'raspberry', 'apple', 'coconut', 'banana'
        ]).find_most_similar('berry'), 'cherry')

    def test_equal_3(self):
        self.assertEqual(Dictionary([
            'cherry', 'peach', 'pineapple', 'melon', 'strawberry',
            'raspberry', 'apple', 'coconut', 'banana'
        ]).find_most_similar('aple'), 'apple')

    def test_equal_4(self):
        self.assertEqual(Dictionary([
            'javascript', 'c', 'php', 'cpp', 'java', 'ruby', 'coffeescript',
            'python', 'brainfuck'
        ]).find_most_similar('heaven'), 'java')

    def test_equal_5(self):
        self.assertEqual(Dictionary([
            'javascript', 'c', 'php', 'cpp', 'java', 'ruby', 'coffeescript',
            'python', 'brainfuck'
        ]).find_most_similar('javascript'), 'javascript')

    def test_equal_6(self):
        self.assertEqual(Dictionary([
            'code', 'mars', 'codewars', 'wars', 'codec', 'stars'
        ]).find_most_similar('coddwars'), 'codewars')

    def test_equal_7(self):
        self.assertEqual(Dictionary([
            'xikoctmrhpvi', 'ggcvrtxrtnafw', 'pxyousorusjxxbt',
            'loogviwcojxgvi', 'ntwmwwmicnjvhtt', 'ajacizfrgxfumzpvi',
            'tdvibqccxr', 'fxpvfhfrujjaifr', 'dihhiczkdwiofpr', 'qojfrlhufr',
            'znystgvifufptxr', 'kqijoorfkejdcxr', 'psaysnhfrrqgxwik',
            'lnjhrzfrosinb', 'fgtrjakzlnaebxr', 'mhmkakybpczjbb',
            'riyhpvimgaliuxr', 'vkholxrvjwisrk', 'afirbipbmkamjzw',
            'cfvruditwcxr', 'iqkyztorburjgiudi', 'clxmqmiycvidiyr',
            'xffrkbdyjveb', 'hrwuhmtxxvmygb', 'nnsoamjkrzgldi',
            'hkldhadcxrjbmkmcdi', 'jhjyasikwyufr', 'ljxzjjorwgb',
            'dyhxgviphoptak', 'npyrgrpbdfqhhncdi', 'fxjskybblljqr',
            'emvquxrvvlvwvsi', 'hirldidcuzbyb', 'hwzsemiqxjwfk',
            'sefsknopiffajor', 'ucxmdeudiycokfnb', 'zqdrhpviqslik',
            'xrgdgqfrldwk', 'ppctybxgtleipb', 'eglanhfredaykxr',
            'cpnqknjyviusknmte', 'karpscdigdvucfr', 'cwhyyzaorpvtnlfr',
            'xuwahveztwoor', 'pdyjrkaylryr', 'jcocndjkyb', 'qifwqgdsijibor',
            'tklquxrnhfiggb', 'osbednerciaai', 'iroezmixmberfr'
        ]).find_most_similar('rkacypviuburk'), 'zqdrhpviqslik')

    def test_equal_8(self):
        self.assertEqual(Dictionary([
            'Gamilas', 'Gatlantis', 'Denguil', 'Nebula', 'Earth'
        ]).find_most_similar('Eart'), 'Earth')

    def test_equal_9(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Bolar', 'Galman', 'Gatlantis', 'Iscandar'
        ]).find_most_similar('scandar'), 'Iscandar')

    def test_equal_10(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Earth', 'Bolar', 'Galman', 'Gatlantis'
        ]).find_most_similar('BolaT'), 'Bolar')

    def test_equal_11(self):
        self.assertEqual(Dictionary([
            'Iscandar', 'Aquarius', 'Nebula', 'Bolar', 'Shalbart'
        ]).find_most_similar('Bolar'), 'Bolar')

    def test_equal_12(self):
        self.assertEqual(Dictionary([
            'Shalbart', 'Gamilas', 'Gatlantis', 'Bolar', 'Galman'
        ]).find_most_similar('S-albart'), 'Shalbart')

    def test_equal_13(self):
        self.assertEqual(Dictionary([
            'Iscandar', 'Denguil', 'Gatlantis', 'Nebula', 'Gamilas'
        ]).find_most_similar('NebUla'), 'Nebula')

    def test_equal_14(self):
        self.assertEqual(Dictionary([
            'Aquarius', 'Earth', 'Nebula', 'Gamilas', 'Galman'
        ]).find_most_similar('Galmn'), 'Galman')

    def test_equal_15(self):
        self.assertEqual(Dictionary([
            'Aquarius', 'Denguil', 'Galman', 'Nebula', 'Gamilas'
        ]).find_most_similar('Gaman'), 'Galman')

    def test_equal_16(self):
        self.assertEqual(Dictionary([
            'Shalbart', 'Denguil', 'Telezart', 'Bolar', 'Gamilas'
        ]).find_most_similar('TelezIart'), 'Telezart')

    def test_equal_17(self):
        self.assertEqual(Dictionary([
            'Bolar', 'Denguil', 'Galman', 'Iscandar', 'Nebula'
        ]).find_most_similar('Galgan'), 'Galman')

    def test_equal_18(self):
        self.assertEqual(Dictionary([
            'Aquarius', 'Bolar', 'Gamilas', 'Galman', 'Earth'
        ]).find_most_similar('arth'), 'Earth')

    def test_equal_19(self):
        self.assertEqual(Dictionary([
            'Gamilas', 'Earth', 'Gatlantis', 'Telezart', 'Nebula'
        ]).find_most_similar('atlantis'), 'Gatlantis')

    def test_equal_20(self):
        self.assertEqual(Dictionary([
            'Aquarius', 'Bolar', 'Denguil', 'Nebula', 'Gamilas'
        ]).find_most_similar('Gamiwlas'), 'Gamilas')

    def test_equal_21(self):
        self.assertEqual(Dictionary([
            'Iscandar', 'Galman', 'Bolar', 'Earth', 'Nebula'
        ]).find_most_similar('Eath'), 'Earth')

    def test_equal_22(self):
        self.assertEqual(Dictionary([
            'Nebula', 'Bolar', 'Shalbart', 'Galman', 'Telezart'
        ]).find_most_similar('Nbula'), 'Nebula')

    def test_equal_23(self):
        self.assertEqual(Dictionary([
            'Galman', 'Aquarius', 'Shalbart', 'Nebula', 'Earth'
        ]).find_most_similar('Shalbgrt'), 'Shalbart')

    def test_equal_24(self):
        self.assertEqual(Dictionary([
            'Telezart', 'Gamilas', 'Earth', 'Denguil', 'Gatlantis'
        ]).find_most_similar('Ebarth'), 'Earth')

    def test_equal_25(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Bolar', 'Telezart', 'Iscandar', 'Nebula'
        ]).find_most_similar('Nebla'), 'Nebula')

    def test_equal_26(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Telezart', 'Nebula', 'Bolar', 'Earth'
        ]).find_most_similar('Deguil'), 'Denguil')

    def test_equal_27(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Bolar', 'Gatlantis', 'Telezart', 'Shalbart'
        ]).find_most_similar('Gatlantiys'), 'Gatlantis')

    def test_equal_28(self):
        self.assertEqual(Dictionary([
            'Nebula', 'Telezart', 'Galman', 'Earth', 'Aquarius'
        ]).find_most_similar('Galma'), 'Galman')

    def test_equal_29(self):
        self.assertEqual(Dictionary([
            'Gatlantis', 'Galman', 'Telezart', 'Gamilas', 'Aquarius'
        ]).find_most_similar('Auarius'), 'Aquarius')

    def test_equal_30(self):
        self.assertEqual(Dictionary([
            'Shalbart', 'Gatlantis', 'Bolar', 'Earth', 'Iscandar'
        ]).find_most_similar('Eart'), 'Earth')

    def test_equal_31(self):
        self.assertEqual(Dictionary([
            'Shalbart', 'Denguil', 'Iscandar', 'Gatlantis', 'Earth'
        ]).find_most_similar('Deguil'), 'Denguil')

    def test_equal_32(self):
        self.assertEqual(Dictionary([
            'Galman', 'Telezart', 'Gatlantis', 'Iscandar', 'Shalbart'
        ]).find_most_similar('Gatlatis'), 'Gatlantis')

    def test_equal_33(self):
        self.assertEqual(Dictionary([
            'Shalbart', 'Bolar', 'Telezart', 'Galman', 'Nebula'
        ]).find_most_similar('Teleart'), 'Telezart')

    def test_equal_34(self):
        self.assertEqual(Dictionary([
            'Nebula', 'Iscandar', 'Gatlantis', 'Gamilas', 'Aquarius'
        ]).find_most_similar('Gamils'), 'Gamilas')

    def test_equal_35(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Shalbart', 'Nebula', 'Telezart', 'Earth'
        ]).find_most_similar('DenguEl'), 'Denguil')

    def test_equal_36(self):
        self.assertEqual(Dictionary([
            'Aquarius', 'Galman', 'Gamilas', 'Earth', 'Shalbart'
        ]).find_most_similar('Shalbar'), 'Shalbart')

    def test_equal_37(self):
        self.assertEqual(Dictionary([
            'Iscandar', 'Gatlantis', 'Nebula', 'Galman', 'Denguil'
        ]).find_most_similar('Nebla'), 'Nebula')

    def test_equal_38(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Gamilas', 'Bolar', 'Galman', 'Aquarius'
        ]).find_most_similar('Dengil'), 'Denguil')

    def test_equal_39(self):
        self.assertEqual(Dictionary([
            'Telezart', 'Aquarius', 'Shalbart', 'Gatlantis', 'Earth'
        ]).find_most_similar('Gatlanis'), 'Gatlantis')

    def test_equal_40(self):
        self.assertEqual(Dictionary([
            'Bolar', 'Shalbart', 'Gatlantis', 'Denguil', 'Aquarius'
        ]).find_most_similar('Shalbalt'), 'Shalbart')

    def test_equal_41(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Bolar', 'Gamilas', 'Telezart', 'Galman'
        ]).find_most_similar('Bola'), 'Bolar')

    def test_equal_42(self):
        self.assertEqual(Dictionary([
            'Bolar', 'Iscandar', 'Telezart', 'Denguil', 'Galman'
        ]).find_most_similar('Iscanddar'), 'Iscandar')

    def test_equal_43(self):
        self.assertEqual(Dictionary([
            'Bolar', 'Gatlantis', 'Aquarius', 'Denguil', 'Galman'
        ]).find_most_similar('Gaman'), 'Galman')

    def test_equal_44(self):
        self.assertEqual(Dictionary([
            'Gatlantis', 'Nebula', 'Telezart', 'Bolar', 'Denguil'
        ]).find_most_similar('Tlezart'), 'Telezart')

    def test_equal_45(self):
        self.assertEqual(Dictionary([
            'Gamilas', 'Shalbart', 'Aquarius', 'Telezart', 'Nebula'
        ]).find_most_similar('Aqarius'), 'Aquarius')

    def test_equal_46(self):
        self.assertEqual(Dictionary([
            'Denguil', 'Earth', 'Nebula', 'Gamilas', 'Aquarius'
        ]).find_most_similar('DenguOl'), 'Denguil')

    def test_equal_47(self):
        self.assertEqual(Dictionary([
            'Shalbart', 'Iscandar', 'Gamilas', 'Aquarius', 'Gatlantis'
        ]).find_most_similar('Iscanar'), 'Iscandar')
