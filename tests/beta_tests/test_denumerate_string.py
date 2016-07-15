import unittest

from katas.beta.denumerate_string import denumerate


class DenumerateTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(denumerate([
            (4, 'y'), (1, 'o'), (3, 't'), (0, 'm'), (2, 'n')
        ]), 'monty')

    def test_equal_2(self):
        self.assertEqual(denumerate([
            (1, '3'), (2, 'l'), (4, 'o'), (3, 'l'), (0, 'h')
        ]), 'h3llo')

    def test_false_1(self):
        self.assertFalse(denumerate([(0, '%')]))

    def test_false_2(self):
        self.assertFalse(denumerate([(1, 'a'), (2, 'b')]))
