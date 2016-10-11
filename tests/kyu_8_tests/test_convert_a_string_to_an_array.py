import unittest

from katas.kyu_8.convert_a_string_to_an_array import string_to_array


class StringToArrayTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(string_to_array('Robin Singh'), ['Robin', 'Singh'])

    def test_equal_2(self):
        self.assertEqual(string_to_array('CodeWars'), ['CodeWars'])

    def test_equal_3(self):
        self.assertEqual(string_to_array('I love arrays they are my favorite'),
                         ['I', 'love', 'arrays', 'they', 'are', 'my',
                          'favorite'])

    def test_equal_4(self):
        self.assertEqual(string_to_array('1 2 3'), ['1', '2', '3'])

    def test_equal_5(self):
        self.assertEqual(string_to_array(''), [''])
