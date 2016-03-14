import unittest

from katas.kyu_6.turkish_national_identity_number import check_valid_tr_number


class TurkishNationalIdentityNumberTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_valid_tr_number(36637640050))

    def test_true_2(self):
        self.assertTrue(check_valid_tr_number(10000000146))

    def test_true_3(self):
        self.assertTrue(check_valid_tr_number(10167994524))

    def test_false(self):
        self.assertFalse(check_valid_tr_number(6923522112))

    def test_false_2(self):
        self.assertFalse(check_valid_tr_number(692352217312))

    def test_false_3(self):
        self.assertFalse(check_valid_tr_number('x5810a78432'))

    def test_false_4(self):
        self.assertFalse(check_valid_tr_number(12762438338))


if __name__ == '__main__':
    unittest.main()
