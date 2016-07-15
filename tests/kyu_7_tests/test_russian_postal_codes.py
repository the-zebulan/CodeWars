import unittest

from katas.kyu_7.russian_postal_codes import zip_validate


class ZipValidateTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(zip_validate('198328'))

    def test_true_2(self):
        self.assertTrue(zip_validate('310003'))

    def test_true_3(self):
        self.assertTrue(zip_validate('424000'))

    def test_false(self):
        self.assertFalse(zip_validate('12A483'))

    def test_false_2(self):
        self.assertFalse(zip_validate('1@63'))

    def test_false_3(self):
        self.assertFalse(zip_validate('111'))

    def test_false_4(self):
        self.assertFalse(zip_validate('056879'))

    def test_false_5(self):
        self.assertFalse(zip_validate('1111111'))
