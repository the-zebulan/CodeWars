import unittest

from katas.kyu_7.composing_squared_strings import compose


class ComposeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(compose(
            'byGt\nhTts\nRTFF\nCnnI', 'jIRl\nViBu\nrWOb\nNkTB'
        ), 'bNkTB\nhTrWO\nRTFVi\nCnnIj')

    def test_equal_2(self):
        self.assertEqual(compose(
            'HXxA\nTGBf\nIPhg\nuUMD', 'Hcbj\nqteH\nGbMJ\ngYPW'
        ), 'HgYPW\nTGGbM\nIPhqt\nuUMDH')

    def test_equal_3(self):
        self.assertEqual(compose(
            'tSrJ\nOONy\nsqPF\nxMkB', 'hLqw\nEZuh\nmYFl\nzlYf'
        ), 'tzlYf\nOOmYF\nsqPEZ\nxMkBh')

    def test_equal_4(self):
        self.assertEqual(compose('fn\nlr', 'Kz\nmO'), 'fmO\nlrK')

    def test_equal_5(self):
        self.assertEqual(compose(
            'fctRKq\nBCorKQ\nZKGbDO\nbhHohe\nUjyNSg\nPCOiuM',
            'elSYAB\nLQMYuN\nTzQtaM\nFutqip\nwSAjZX\nuOPhSJ'
        ), 'fuOPhSJ\nBCwSAjZ\nZKGFutq\nbhHoTzQ\nUjyNSLQ\nPCOiuMe')

    def test_equal_6(self):
        self.assertEqual(compose(
            'lFqaEC\nITEzHC\nqaEPEb\nexhzgU\nxoxRJc\nTxqlDN',
            'IMpAnn\nktLyDb\nHawiQt\nNVRips\ncrKROc\nJqPpty'
        ), 'lJqPpty\nITcrKRO\nqaENVRi\nexhzHaw\nxoxRJkt\nTxqlDNI')

    def test_equal_7(self):
        self.assertEqual(compose(
            'RCKr\naJwU\nqEyM\nNbdP', 'hxYA\nlUtD\nLFmc\nssTy'
        ), 'RssTy\naJLFm\nqEylU\nNbdPh')

    def test_equal_8(self):
        self.assertEqual(compose(
            'qtKz\negiP\niOgb\nRqly', 'ZUCx\nShBJ\nmybK\neBZA'
        ), 'qeBZA\negmyb\niOgSh\nRqlyZ')

    def test_equal_9(self):
        self.assertEqual(compose(
            'rmNE\naFQJ\nfsNe\ntDtw', 'GvqU\noJlZ\ngJxQ\nVQvX'
        ), 'rVQvX\naFgJx\nfsNoJ\ntDtwG')

    def test_equal_10(self):
        self.assertEqual(compose(
            'wEGa\nhICc\nPrvY\nCuSd', 'qfYz\nwJfU\noHhO\nNxaV'
        ), 'wNxaV\nhIoHh\nPrvwJ\nCuSdq')
