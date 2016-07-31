import unittest

from katas.kyu_8.add_length import add_length


class AddLengthTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(add_length('apple ban'), ['apple 5', 'ban 3'])

    def test_equal_2(self):
        self.assertEqual(add_length('you will win'),
                         ['you 3', 'will 4', 'win 3'])

    def test_equal_3(self):
        self.assertEqual(add_length('you'), ['you 3'])

    def test_equal_4(self):
        self.assertEqual(add_length('y'), ['y 1'])
