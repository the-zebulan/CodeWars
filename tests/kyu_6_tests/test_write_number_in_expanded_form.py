import unittest

from katas.kyu_6.write_number_in_expanded_form import expanded_form


class ExpandedFormTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(expanded_form(12), '10 + 2')

    def test_equal_2(self):
        self.assertEqual(expanded_form(42), '40 + 2')

    def test_equal_3(self):
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')
