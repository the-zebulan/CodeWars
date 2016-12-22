import unittest

from katas.beta.keep_it_short_with_restrictions import short


class ShortTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(short([{1, 2, 3}, {2, 3, 4}]),
                         {1: 1, 2: 2, 3: 2, 4: 1})

    def test_equal_2(self):
        self.assertEqual(short([{1, 2, 3, 4}]), {1: 1, 2: 1, 3: 1, 4: 1})

    def test_equal_3(self):
        self.assertEqual(short([{1}, {1, 3, 4, 5}]), {1: 2, 3: 1, 4: 1, 5: 1})
