import unittest

from katas.kyu_8.how_do_i_compare_numbers import what_is


class WhatIsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(what_is(0), 'nothing')

    def test_equals_2(self):
        self.assertEqual(what_is(123), 'nothing')

    def test_equals_3(self):
        self.assertEqual(what_is(-1), 'nothing')

    def test_equals_4(self):
        self.assertEqual(what_is(42), 'everything')

    def test_equals_5(self):
        self.assertEqual(what_is(42 * 42), 'everything squared')


if __name__ == '__main__':
    unittest.main()
