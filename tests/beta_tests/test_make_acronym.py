import unittest

from katas.beta.make_acronym import to_acronym


class ToAcronymTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(to_acronym('Code Wars'), 'CW')

    def test_equal_2(self):
        self.assertEqual(to_acronym('Water Closet'), 'WC')

    def test_equal_3(self):
        self.assertEqual(to_acronym('Portable Network Graphics'), 'PNG')

    def test_equal_4(self):
        self.assertEqual(to_acronym('PHP: Hypertext Preprocessor'), 'PHP')

    def test_equal_5(self):
        self.assertEqual(to_acronym('hyper text markup language'), 'HTML')
