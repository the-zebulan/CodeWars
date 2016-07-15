import unittest

from katas.kyu_6.evil_autocorrect_prank import autocorrect


class AutocorrectPrankTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(autocorrect('u'), 'your sister')

    def test_equals_2(self):
        self.assertEqual(autocorrect('you'), 'your sister')

    def test_equals_3(self):
        self.assertEqual(autocorrect('Youuuuu'), 'your sister')

    def test_equals_4(self):
        self.assertEqual(autocorrect('youtube'), 'youtube')

    def test_equals_5(self):
        self.assertEqual(autocorrect(
            'You u youville utube you youyouyou uuu raiyou united youuuu u y'
            'ou'),
            'your sister your sister youville utube your sister youyouyou uu'
            'u raiyou united your sister your sister your sister')
