import unittest

from Kyu_6.word_a9n import abbreviate


class AbbreviateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(abbreviate(
            'balloon: double-barreled, sat\'mat: sits, a-on, mat\'the, '),
            'b5n: d4e-b6d, sat\'mat: s2s, a-on, mat\'the, ')

    def test_equals_2(self):
        self.assertEqual(abbreviate('internationalization'), 'i18n')

    def test_equals_3(self):
        self.assertEqual(abbreviate('accessibility'), 'a11y')

    def test_equals_4(self):
        self.assertEqual(abbreviate('Accessibility'), 'A11y')

    def test_equals_5(self):
        self.assertEqual(abbreviate('elephant-ride'), 'e6t-r2e')


if __name__ == '__main__':
    unittest.main()
