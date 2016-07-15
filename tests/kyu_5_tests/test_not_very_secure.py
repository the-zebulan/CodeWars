import unittest

from katas.kyu_5.not_very_secure import alphanumeric


class AlphaNumericTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(alphanumeric('PassW0rd'))

    def test_false(self):
        self.assertFalse(alphanumeric('hello world_'))

    def test_false_2(self):
        self.assertFalse(alphanumeric('     '))
