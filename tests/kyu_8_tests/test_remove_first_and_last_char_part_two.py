import unittest

from katas.kyu_8.remove_first_and_last_char_part_two import array


class ArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(array('1,2,3'), '2')

    def test_equals_2(self):
        self.assertEqual(array('1,2,3,4'), '2 3')

    def test_none(self):
        self.assertIsNone(array(''))

    def test_none_2(self):
        self.assertIsNone(array('1'))

    def test_none_3(self):
        self.assertIsNone(array('1, 3'))
