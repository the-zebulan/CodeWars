import unittest

from katas.kyu_7.spoonerize_me import spoonerize


class SpoonerizeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(spoonerize('nit picking'), 'pit nicking')

    def test_equals_2(self):
        self.assertEqual(spoonerize('wedding bells'), 'bedding wells')

    def test_equals_3(self):
        self.assertEqual(spoonerize('jelly beans'), 'belly jeans')

    def test_equals_4(self):
        self.assertEqual(spoonerize('pop corn'), 'cop porn')
