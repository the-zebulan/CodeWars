import unittest

from katas.kyu_7.reversed_strings import solution


class ReversedStringsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution('world'), 'dlrow')

    def test_equals_2(self):
        self.assertEqual(solution('hello'), 'olleh')

    def test_equals_3(self):
        self.assertEqual(solution(''), '')

    def test_equals_4(self):
        self.assertEqual(solution('h'), 'h')
