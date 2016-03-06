import unittest

from Kyu_7.javascript_filter_1 import search_names


class SearchNamesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(search_names(
            [['foo', 'foo@foo.com'], ['bar_', 'bar@bar.com']]
        ), [['bar_', 'bar@bar.com']])


if __name__ == '__main__':
    unittest.main()
