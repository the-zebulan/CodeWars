import unittest

from katas.kyu_6.scrabble_best_word import get_best_word


class GetBestWordTestCase(unittest.TestCase):
    def setUp(self):
        self.points = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 10, 1, 2, 1,
                       1, 3, 8, 1, 1, 1, 1, 4, 10, 10, 10, 10)

    def test_equals(self):
        self.assertEqual(get_best_word(
            self.points, ['WHO', 'IS', 'THE', 'BEST', 'OF', 'US']), 0)

    def test_equals_2(self):
        self.assertEqual(get_best_word(
            self.points, ['NOQ', 'TXAY', 'S', 'OM', 'ESFT', 'CJUKQ', 'QL',
                          'QO', 'ASTK', 'Y']), 5)

    def test_equals_3(self):
        self.assertEqual(get_best_word(self.points, [
            'N', 'AO', 'TQGZW', 'P', 'OBTP', 'CLWXB', 'Y', 'JQGFJ', 'Q', 'RP',
            'OC', 'MRQCZ', 'ZWN', 'ZRT', 'OIRYH', 'GWPMSZP', 'LQRYUKQ', 'LBM',
            'LFEI', 'VHUX', 'RTALLIC', 'JEMUPS', 'XUW', 'X', 'ZLXFMWS',
            'LFAGR', 'HJ', 'RTUAI', 'JRBNG', 'ZUYSC', 'CIEYV', 'FUY', 'B',
            'EJS', 'CINBTQS', 'JEAC', 'JX', 'LLILSEK', 'W', 'KLUV']), 16)

    def test_equals_4(self):
        self.assertEqual(get_best_word(self.points, [
            'SVWLIDP', 'FCPKTHW', 'EREMN', 'NFEF', 'PQ', 'FSC', 'ZYPOSXJ',
            'BOR', 'YCGG', 'RC', 'DVPE', 'VAOE', 'OIGK', 'OTQE', 'REJFUFD',
            'FVBCSSB', 'VHJ', 'BEC', 'MWZQ', 'WX', 'L', 'ZPCB', 'JKLHE',
            'RYFTY', 'NKP', 'ID', 'O', 'KA', 'VRXX', 'NTDB', 'OERKPC',
            'YFLUI', 'SKQCJ', 'PXDSW', 'ITYWD', 'TC', 'LOIDQEJ', 'NE', 'YND',
            'VJHOCEC', 'RPRANZ', 'BQ', 'STM', 'RGVBFW', 'SMWUYLW', 'KT',
            'SXHY', 'XCE', 'T', 'SC', 'UDJU', 'CHDR', 'UGXNQ', 'CQOOBA', 'O',
            'NWW', 'V', 'L', 'BAQ', 'AZN', 'LBTR', 'N', 'QSURR', 'KADPH', 'M',
            'LCBEAKM', 'ZHEVXS', 'F', 'TVAIQCY', 'MF', 'KCI', 'YQ', 'RCG',
            'AKYPCP', 'WJXG', 'RQXOI', 'SJI', 'TWXZ', 'J', 'HIKCGHV',
            'EAAXGG', 'AETSH', 'EO', 'BUET', 'TDIQCO', 'TKL', 'FJCRY',
            'ZHAJLK', 'OLMCVA', 'F']), 6)

    def test_equals_5(self):
        self.assertEqual(get_best_word(self.points, [
            'RBBL', 'ZJ', 'ZOFXE', 'LMBFCFX', 'O', 'JG', 'SYRYE', 'VXG', 'EU',
            'DAIFZR', 'BQUNZHH', 'WKO', 'TFPHPLX', 'SWLG', 'CY', 'JYQNDSM',
            'ITPS', 'B', 'UVSDMWR', 'LCPS']), 15)

    def test_equals_6(self):
        self.assertEqual(get_best_word(self.points, [
            'LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ',
            'BB', 'IVVLXBC', 'ZRENSWMG']), 5)
