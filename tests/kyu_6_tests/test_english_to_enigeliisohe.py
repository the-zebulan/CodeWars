import unittest

from katas.kyu_6.english_to_enigeliisohe import toexuto


class ToexutoTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(toexuto('little'), 'liitotolie')

    def test_equals_2(self):
        self.assertEqual(toexuto('BIG'), 'BaIGe')

    def test_equals_3(self):
        self.assertEqual(toexuto(
            'This is a test. This is only a test.'),
            'Toheiso iso a toesoto. Toheiso iso oniliyu a toesoto.')
