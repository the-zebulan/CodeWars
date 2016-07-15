import unittest

from katas.beta.caesar_cipher import caesar


class CaesarTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(caesar('Abcd', 2), 'Cdef')

    def test_equals_2(self):
        self.assertEqual(caesar('message', -1), 'ldrrzfd')

    def test_equals_3(self):
        self.assertEqual(caesar('ZZ Top', 3), 'CC Wrs')
