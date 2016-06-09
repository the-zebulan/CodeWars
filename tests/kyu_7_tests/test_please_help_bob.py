import unittest

from katas.kyu_7.please_help_bob import err_bob


class BobTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(err_bob('r r r r r r r r'),
                         'rerr rerr rerr rerr rerr rerr rerr rerr')

    def test_equal_2(self):
        self.assertEqual(err_bob('THIS, is crazy!'),
                         'THISERR, iserr crazyerr!')

    def test_equal_3(self):
        self.assertEqual(err_bob('hI, hi. hI hi skY! sky? skY sky'),
                         'hI, hi. hI hi skYERR! skyerr? skYERR skyerr')

    def test_equal_4(self):
        self.assertEqual(err_bob('Hello, I am Mr Bob.'),
                         'Hello, I amerr Mrerr Boberr.')

    def test_equal_5(self):
        self.assertEqual(err_bob(
            'This, is. another! test? case to check your beautiful code.'
        ), 'Thiserr, iserr. anothererr! testerr? case to checkerr yourerr b'
           'eautifulerr code.')

    def test_equal_6(self):
        self.assertEqual(err_bob(
            'Punctuation? is, important!  double space also'
        ), 'Punctuationerr? iserr, importanterr!  double space also')

    def test_equal_7(self):
        self.assertEqual(err_bob('Hello from the other siiiiideeee'),
                         'Hello fromerr the othererr siiiiideeee')


if __name__ == '__main__':
    unittest.main()
