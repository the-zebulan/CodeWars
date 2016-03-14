import unittest

from katas.kyu_7.make_acronym import make_acronym


class MakeAcronymTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(make_acronym('Hello codewarrior'), 'HC')

    def test_equals_2(self):
        self.assertEqual(make_acronym('a42'), 'Not letters')

    def test_equals_3(self):
        self.assertEqual(make_acronym(42), 'Not a string')

    def test_equals_4(self):
        self.assertEqual(make_acronym([2, 12]), 'Not a string')

    def test_equals_5(self):
        self.assertEqual(make_acronym({'name': 'Abraham'}), 'Not a string')


if __name__ == '__main__':
    unittest.main()
