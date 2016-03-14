import unittest

from kyu_6.format_a_string_of_names import namelist


class NameListTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(namelist([
            {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]),
            'Bart, Lisa & Maggie')

    def test_equals_2(self):
        self.assertEqual(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]),
                         'Bart & Lisa')

    def test_equals_3(self):
        self.assertEqual(namelist([{'name': 'Bart'}]), 'Bart')

    def test_equals_4(self):
        self.assertEqual(namelist([]), '')


if __name__ == '__main__':
    unittest.main()
