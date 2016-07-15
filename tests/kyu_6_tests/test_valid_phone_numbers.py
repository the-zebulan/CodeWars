import unittest

from katas.kyu_6.valid_phone_numbers import validPhoneNumber


class ValidPhoneNumberTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validPhoneNumber('(123) 456-7890'))

    def test_false(self):
        self.assertFalse(validPhoneNumber('(1111)555 2345'))

    def test_false_2(self):
        self.assertFalse(validPhoneNumber('(098) 123 4567'))

    def test_false_3(self):
        self.assertFalse(validPhoneNumber('(123) 456-7890abc'))
