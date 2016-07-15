import unittest

from katas.kyu_8.grasshopper_combine_strings import combine_names


class CombineNamesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(combine_names('James', 'Stevens'), 'James Stevens')

    def test_equals_2(self):
        self.assertEqual(combine_names('Davy', 'Back'), 'Davy Back')

    def test_equals_3(self):
        self.assertEqual(combine_names('Arthur', 'Dent'), 'Arthur Dent')
