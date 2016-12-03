import unittest

from katas.beta.phonewords import phonewords


class PhoneWordsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(phonewords('888'),
                         ['TTT', 'TTU', 'TTV', 'TUT', 'TUU', 'TUV', 'TVT',
                          'TVU', 'TVV', 'UTT', 'UTU', 'UTV', 'UUT', 'UUU',
                          'UUV', 'UVT', 'UVU', 'UVV', 'VTT', 'VTU', 'VTV',
                          'VUT', 'VUU', 'VUV', 'VVT', 'VVU', 'VVV'])

    def test_equal_2(self):
        self.assertEqual(phonewords('34'),
                         ['DG', 'DH', 'DI', 'EG', 'EH', 'EI', 'FG', 'FH',
                          'FI'])

    def test_in_1(self):
        self.assertIn('W00TORKD0W', phonewords('9008675309'))
