import unittest

from katas.kyu_7.bobs_short_forms import short_form


class ShortFormTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(short_form('typhoid'), 'typhd')

    def test_equals_2(self):
        self.assertEqual(short_form('fire'), 'fre')

    def test_equals_3(self):
        self.assertEqual(short_form('destroy'), 'dstry')

    def test_equals_4(self):
        self.assertEqual(short_form('kata'), 'kta')

    def test_equals_5(self):
        self.assertEqual(short_form('codewars'), 'cdwrs')

    def test_equals_6(self):
        self.assertEqual(short_form('assert'), 'assrt')

    def test_equals_7(self):
        self.assertEqual(short_form('insane'), 'insne')

    def test_equals_8(self):
        self.assertEqual(short_form('nice'), 'nce')

    def test_equals_9(self):
        self.assertEqual(short_form('amazing'), 'amzng')

    def test_equals_10(self):
        self.assertEqual(short_form('incorrigible'), 'incrrgble')

    def test_equals_11(self):
        self.assertEqual(short_form('HeEllO'), 'HllO')

    def test_equals_12(self):
        self.assertEqual(short_form('inCRediBLE'), 'inCRdBLE')

    def test_equals_13(self):
        self.assertEqual(short_form('IMpOsSiblE'), 'IMpsSblE')

    def test_equals_14(self):
        self.assertEqual(short_form('UnInTENtiONAl'), 'UnnTNtNl')

    def test_equals_15(self):
        self.assertEqual(short_form('AWESOme'), 'AWSme')

    def test_equals_16(self):
        self.assertEqual(short_form('rhythm'), 'rhythm')

    def test_equals_17(self):
        self.assertEqual(short_form('hymn'), 'hymn')

    def test_equals_18(self):
        self.assertEqual(short_form('lynx'), 'lynx')

    def test_equals_19(self):
        self.assertEqual(short_form('nymph'), 'nymph')

    def test_equals_20(self):
        self.assertEqual(short_form('pygmy'), 'pygmy')


if __name__ == '__main__':
    unittest.main()
