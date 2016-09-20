import unittest

from katas.kyu_7.replace_all_items import replace_all


class ReplaceAllTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(replace_all([], 1, 2), [])

    def test_equal_2(self):
        self.assertEqual(replace_all([1, 2, 2], 1, 2), [2, 2, 2])

    def test_equal_3(self):
        self.assertEqual(replace_all([1, 1, 2], 1, 2), [2, 2, 2])

    def test_equal_4(self):
        self.assertEqual(replace_all([1, 2, 1, 2, 3], 1, 2), [2, 2, 2, 2, 3])

    def test_equal_5(self):
        self.assertEqual(replace_all('Hello World', 'o', '0'), 'Hell0 W0rld')
